from django.http import JsonResponse
from django.views import View
import cohere
import json
import os
from django.conf import settings
from core.cohereIA.models import DatasetBIAS
from cohere.finetuning import BaseModel, FinetunedModel, Hyperparameters, Settings, WandbConfig
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.cohereIA.models import DatasetBIAS
from asgiref.sync import sync_to_async
import asyncio
from datetime import datetime

from core.cohereIA.models import DatasetBIAS, CurrentCohereIA
from core.cohereIA.serializers import DatasetBIASSerializer, CurrentCohereIASerializer

class DatasetBIASViewSet(ModelViewSet):
    queryset = DatasetBIAS.objects.all()
    serializer_class = DatasetBIASSerializer

class CurrentCohereIAViewSet(ModelViewSet):
    queryset = CurrentCohereIA.objects.all()
    serializer_class = CurrentCohereIASerializer


COHERE_API_KEY = settings.COHERE_API_KEY

class GenerateAndTrainModel(APIView):
    async def generate_and_train(self, request):
        try:
            data = json.loads(request.body)
            project_name = data.get("project_name", "default-project") 

            dataset_records = await sync_to_async(DatasetBIAS.objects.all)()

            dataset_file_path = os.path.join('core', 'cohereIA', 'resources', 'dataset.jsonl')
            await sync_to_async(self.create_jsonl_file)(dataset_records, dataset_file_path)

            co = cohere.AsyncClient(api_key=COHERE_API_KEY)

            async def upload_dataset():
                response = await co.datasets.create(
                    name="chat-dataset",
                    data=open(dataset_file_path, "rb"),
                    type="single-label-classification-finetune-input"
                )
                response = await co.wait(response)
                return response

            response = await upload_dataset()
            dataset_id = response.dataset.id

            co = cohere.Client(api_key=COHERE_API_KEY)

            hp = Hyperparameters(
                early_stopping_patience=10,
                early_stopping_threshold=0.001,
                train_batch_size=16,
                train_epoch=1,
                learning_rate=0.01,
            )

            unique_model_name = f"finetuned-model-{datetime.now().strftime('%Y%m%d%H%M%S')}"

            wnb_config = WandbConfig(
                project=project_name,
                api_key=COHERE_API_KEY,
                entity="test-entity",
            )

            finetuned_model = co.finetuning.create_finetuned_model(
                request=FinetunedModel(
                    name=unique_model_name,
                    settings=Settings(
                        base_model=BaseModel(base_type="BASE_TYPE_CLASSIFICATION"),
                        dataset_id=dataset_id,
                        wandb=wnb_config,
                    ),
                )
            )

            await sync_to_async(self.update_current_model)(
                current_model=finetuned_model.finetuned_model.id,
                current_dataset=dataset_id,
                current_name=project_name,
            )

            return {
                'status': 'success',
                'dataset_id': dataset_id,
                'finetuned_model': finetuned_model
            }

        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

    def post(self, request, *args, **kwargs):
        loop = asyncio.new_event_loop()
        result = loop.run_until_complete(self.generate_and_train(request))

        if result['status'] == 'success':
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create_jsonl_file(self, dataset_records, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            for record in dataset_records:
                record_dict = {
                    'text': record.text,
                    'label': record.label
                }
                f.write(json.dumps(record_dict, ensure_ascii=False) + "\n")

    def update_current_model(self, current_model, current_dataset, current_name):
        """
        Atualiza os campos do primeiro item de CurrentCohereIA.
        Se não existir, cria um novo registro.
        """
        obj, created = CurrentCohereIA.objects.get_or_create(
            id=1,  # Presume-se que o primeiro item sempre terá id=1
            defaults={
                'currentModel': current_model,
                'currentDataset': current_dataset,
                'currentName': current_name,
            }
        )
        if not created:
            obj.currentModel = current_model
            obj.currentDataset = current_dataset
            obj.currentName = current_name
            obj.save()


class ClassifyTextView(APIView):
    """
    API View para classificar textos usando o modelo de classificação da Cohere.
    """

    def get(self, request, *args, **kwargs):
        """
        Método GET para verificar o status da API ou retornar informações gerais.
        """
        try:
            # Obtém o modelo atual salvo na tabela CurrentCohereIA
            current_model = CurrentCohereIA.objects.first()

            if current_model:
                model_id = current_model.currentModel
            else:
                return JsonResponse(
                    {
                        "status": "error",
                        "message": "Nenhum modelo atual foi configurado.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            return JsonResponse(
                {
                    "status": "success",
                    "message": "API para classificação de texto está ativa.",
                    "model_id": model_id,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request, *args, **kwargs):
        """
        Método POST para classificar textos.
        """
        try:
            input_text = request.data.get("input_text", "")

            if not input_text:
                return JsonResponse(
                    {"status": "error", "message": "O campo 'input_text' é obrigatório."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            current_model = CurrentCohereIA.objects.first()

            if not current_model:
                return JsonResponse(
                    {
                        "status": "error",
                        "message": "Nenhum modelo atual foi configurado.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            model_id = current_model.currentModel

            # Inicializa o cliente Cohere
            co = cohere.Client(COHERE_API_KEY)

            # Realiza a classificação
            response = co.classify(
                model="6c419c46-f7b4-4dc4-986e-7519a8cc002d-ft",
                inputs=[input_text],
            )

            # Prepara e retorna a resposta
            return JsonResponse(
                {
                    "status": "success",
                    "response": {
                        "classifications": [
                            {
                                "input": classification.input,
                                "prediction": classification.prediction,
                                "confidence": classification.confidence,
                            }
                            for classification in response.classifications
                        ]
                    },
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

