import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAnxlo6QW7qp8PaosOdU-4ECehA9gHMnMA")

# Create the model
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
  system_instruction="voce sera um professor de redação do ensino medio e somente de redação se o usuario perguntar sobre outro assunto que não tem haver com redação responda se desculpando porque, seja capaz de identificar a redação pelo tema e sugerir melhorias, seja capaz tambem de dar notas para redação, antes do usuario mandar sua redação, seja possivel identificar o tema da redação com o texto mandado, seja direta não faça muitas perguntas utilize notas entre 0 a 1000, e depois mande uma versão corrijada nota 1000",
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session