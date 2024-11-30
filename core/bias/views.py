import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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

        if not input_text:
            return Response(
                {"status": "error", "message": "O campo 'input_text' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
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

            target_url = self.ROUTE_MAPPING.get(prediction)

            if not target_url:
                return Response(
                    {"status": "error", "message": f"Prediction '{prediction}' não mapeado."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

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

            redirect_response = requests.post(target_url, json=payload)
            print("{redirect_response} teste resposne")

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

            return Response(response_data, status=status.HTTP_200_OK)

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
