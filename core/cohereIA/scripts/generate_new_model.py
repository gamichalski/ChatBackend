import os
import json
from django.core.management import setup_environ
from myproject import settings  # Substitua "myproject" pelo nome do seu projeto Django
from core.cohereIA.models import DatasetBIAS  

def setup_django():
    """Configura o Django para rodar fora do contexto do servidor."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    setup_environ(settings)

def export_model_to_jsonl():
    """Exporta os dados da model para um arquivo JSONL."""
    setup_django()

    # Caminho do arquivo JSONL
    output_file = "model_data.jsonl"

    # Busca todos os registros da model
    queryset = DatasetBIAS.objects.all()

    # Abre o arquivo no modo de escrita
    with open(output_file, "w", encoding="utf-8") as f:
        for record in queryset:
            # Converte o registro para dicionário
            record_dict = {
                field.name: getattr(record, field.name)
                for field in DatasetBIAS._meta.fields
            }
            # Salva cada registro em formato JSONL
            f.write(json.dumps(record_dict, ensure_ascii=False) + "\n")

    print(f"Dados exportados com sucesso para {output_file}")

def main():
    """Ponto de entrada do script."""
    export_model_to_jsonl()
