from django.core.management.base import BaseCommand
from core.cohereIA.models import DatasetBIAS
import json
import os

class Command(BaseCommand):
    help = "Exporta a model para JSONL"

    def handle(self, *args, **kwargs):
        # Defina o caminho da pasta de destino
        export_dir = os.path.join('core', 'cohereIA', 'resources')

        # Verifique se a pasta existe, se não, crie-a
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        # Defina o caminho completo do arquivo de saída
        output_file = os.path.join(export_dir, "model_data.jsonl")

        # Obtendo os dados da model
        queryset = DatasetBIAS.objects.all()

        # Escrevendo os dados no arquivo
        with open(output_file, "w", encoding="utf-8") as f:
            for record in queryset:
                # Converte o registro em dicionário, excluindo o campo 'id'
                record_dict = {
                    field.name: getattr(record, field.name)
                    for field in DatasetBIAS._meta.fields
                    if field.name != 'id'  # Omitindo o campo 'id'
                }
                f.write(json.dumps(record_dict, ensure_ascii=False) + "\n")

        # Informando o sucesso da operação
        self.stdout.write(self.style.SUCCESS(f"Dados exportados para {output_file}"))
