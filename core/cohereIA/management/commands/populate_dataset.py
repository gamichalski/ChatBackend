from django.core.management.base import BaseCommand
from core.cohereIA.models import DatasetBIAS  
import json
import os

class Command(BaseCommand):
    help = "Importa dados de um arquivo JSONL para a model Dataset"

    def handle(self, *args, **kwargs):
        
        input_file = os.path.join('core', 'cohereIA', 'resources', 'main_dataset.jsonl')

        if not os.path.exists(input_file):
            self.stdout.write(self.style.ERROR(f"Arquivo {input_file} não encontrado."))
            return

        # Abrindo o arquivo e processando os dados
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    data = json.loads(line.strip())

                    DatasetBIAS.objects.create(
                        text=data.get('text', ''),
                        label=data.get('label', '')
                    )
                    self.stdout.write(self.style.SUCCESS(f"Dados inseridos: {data}"))

                except json.JSONDecodeError as e:
                    self.stdout.write(self.style.ERROR(f"Erro ao processar a linha: {line}"))
                    continue
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erro ao inserir dados: {e}"))
                    continue

        self.stdout.write(self.style.SUCCESS(f"Importação concluída com sucesso!"))
