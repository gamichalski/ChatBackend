from django.core.management.base import BaseCommand
from core.cohereIA.models import DatasetBIAS
import json
import os

class Command(BaseCommand):
    help = "Cria um backup da model Dataset, limpa os registros e insere novos dados de um arquivo JSONL fixo"

    def handle(self, *args, **kwargs):
        # Caminho do arquivo de backup
        backup_dir = os.path.join('core', 'cohereIA', 'backup')
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Arquivo de backup
        backup_file = os.path.join(backup_dir, 'dataset_backup.jsonl')

        # Criação do backup
        queryset = DatasetBIAS.objects.all()
        with open(backup_file, 'w', encoding='utf-8') as f:
            for record in queryset:
                record_dict = {
                    field.name: getattr(record, field.name)
                    for field in DatasetBIAS._meta.fields
                }
                f.write(json.dumps(record_dict, ensure_ascii=False) + "\n")

        # Limpando a model Dataset
        DatasetBIAS.objects.all().delete()

        # Caminho fixo do arquivo de novos dados
        input_file_path = os.path.join('core', 'cohereIA', 'resources', 'main_dataset.jsonl')
        
        if not os.path.exists(input_file_path):
            self.stdout.write(self.style.ERROR(f"Arquivo {input_file_path} não encontrado."))
            return

        # Inserindo novos dados a partir do arquivo JSONL
        with open(input_file_path, 'r', encoding='utf-8') as f:
            data_to_insert = []
            for line in f:
                try:
                    data = json.loads(line.strip())
                    dataset_instance = DatasetBIAS(
                        text=data.get('text', ''),
                        label=data.get('label', '')
                    )
                    data_to_insert.append(dataset_instance)
                except json.JSONDecodeError as e:
                    self.stdout.write(self.style.ERROR(f"Erro ao processar a linha: {line}"))
                    continue

            # Inserindo os dados de uma vez
            if data_to_insert:
                DatasetBIAS.objects.bulk_create(data_to_insert)

        # Mensagem de sucesso
        self.stdout.write(self.style.SUCCESS(f"Backup criado, dados da model Dataset limpos e novos dados inseridos a partir de {input_file_path}."))
