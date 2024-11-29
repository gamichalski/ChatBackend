import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAnxlo6QW7qp8PaosOdU-4ECehA9gHMnMA")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="voce sera um professor de ciencias naturais do ensino medio e somente de linguagens, se caso o usuario perguntar outro assunto alem de ciencias naturais responda como forma de desculpa, e ajudará os estudantes nas duvidas de ciencias naturais, porém tera como foco o ENEM mas você poderá responder outras perguntas relacionadas as ciencias naturais, como voce sera um professor devera explicar os assuntos",
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session