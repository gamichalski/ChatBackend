import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.chat.models import Chat, Answer

class ClassifyMessageView(APIView):
    """
    View para classificar o texto e redirecionar a requisição para a rota correspondente com base no prediction.
    """

    ROUTE_MAPPING = {
        "Linguagens": "http://127.0.0.1:8000/api/languageAI/",
        "Genérico": "http://127.0.0.1:8000/api/genericAI/",
        "Ciencias Humanas": "http://127.0.0.1:8000/api/humanscienceAI/",
        "Ciencias da natureza": "http://127.0.0.1:8000/api/naturalscienceAI/",
        "Ciencias Exatas": "http://127.0.0.1:8000/api/mathAI/",
    }

    def post(self, request, *args, **kwargs):
        """
        Método POST para classificar o texto e redirecionar a requisição.
        """
        input_text = request.data.get("input_text", "")
        recivied_chat = request.data.get('chat_name', '')

        print(recivied_chat)

        try:
            selected_chat = Chat.objects.get(id=recivied_chat)

            if selected_chat.ia is not None:
                ia_type = selected_chat.ia  # Usar o tipo de IA já atribuído

                # Escolha do endpoint com base no tipo de IA já atribuído
                if ia_type == 1:
                    prediction = "Linguagens"
                elif ia_type == 2:
                    prediction = "Ciencias Exatas"
                elif ia_type == 3:
                    prediction = "Ciencias da natureza"
                elif ia_type == 4:
                    prediction = "Ciencias Humanas"
                elif ia_type == 6:
                    prediction = "Genérico"
                else:
                    prediction = None
            else:
                prediction = None  # Caso o valor de IA seja None

            # Caso a previsão não tenha sido definida pelo valor de 'ia' no chat
            if not prediction:
                classify_response = requests.post(
                    "http://127.0.0.1:8000/classify/", json={"input_text": input_text}
                )

                if classify_response.status_code != 200:
                    return Response(
                        {"status": "error", "message": "Erro ao classificar o texto."},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

                classification_data = classify_response.json()
                prediction = classification_data["response"]["classifications"][0]["prediction"]

                # Atribuindo o valor da previsão à variável ia_type
                if prediction == "Linguagens":
                    ia_type = 1
                elif prediction == "Ciencias Exatas":
                    ia_type = 2
                elif prediction == "Ciencias da natureza":
                    ia_type = 3
                elif prediction == "Ciencias Humanas":
                    ia_type = 4
                elif prediction == "Genérico":
                    ia_type = 6
                else:
                    ia_type = 0

            # Atualizar o campo 'ia' no chat com o valor calculado
            selected_chat.ia = ia_type
            selected_chat.save()

            target_url = self.ROUTE_MAPPING.get(prediction)

            if not target_url:
                return Response(
                    {"status": "error", "message": f"Prediction '{prediction}' não mapeado."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Payload a ser enviado ao endpoint correto
            if prediction == "Genérico":
                payload = {
                    "answer": input_text,
                    "response": None,
                    "user": 1,
                }
            else:
                payload = {
                    "user": 1,
                    "cover": None,
                    "answer": input_text,
                }

            # Realiza o POST para a rota alvo
            redirect_response = requests.post(target_url, json=payload)

            if redirect_response.status_code != 201:
                return Response(
                    {"status": "error", "message": f"Erro ao acessar a rota '{target_url}'."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            api_response = redirect_response.json()

            response_data = {
                "tema": prediction,
                "pergunta": input_text,
                "usuario": payload.get("user"),
                "resposta": api_response.get("response", "Resposta não disponível."),
                "status": "success",
                "api": target_url
            }

            message_data = {
                "answer": input_text,
                "response": response_data["resposta"],
                "chat": selected_chat
            }

            output_data = Answer.objects.create(**message_data)

            print(output_data)

            return Response(response_data, status=status.HTTP_200_OK)

        except Chat.DoesNotExist:
            return Response(
                {"status": "error", "message": f"Chat com nome '{recivied_chat}' não encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def get(self, request, *args, **kwargs):
        """
        Método GET para retornar informações da API de classificação.
        """
        try:
            response = requests.get("http://127.0.0.1:8000/classify/")

            if response.status_code != 200:
                return Response(
                    {"status": "error", "message": "Erro ao obter os dados da API externa."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            return Response(response.json(), status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
