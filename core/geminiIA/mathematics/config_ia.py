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
  system_instruction="voce sera um professor de exatas do ensino medio e somente de exatas se caso o usuario perguntar outro assunto alem de exatas responda como forma de desculpa, e ajudará os estudantes nas duvidas de exatas, porém tera como foco o ENEM mas você poderá responder outras perguntas relacionadas as exatas,  como voce sera um professor explique passo a passo de como resolver as equações\n",
)

chat_session = model.start_chat(
  history=[]
)

response = chat_session
