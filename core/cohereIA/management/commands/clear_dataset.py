from django.core.management.base import BaseCommand
from core.cohereIA.models import DatasetBIAS
import json
import os

class Command(BaseCommand):
    help = "Cria um backup da model Dataset e limpa os registros"

    def handle(self, *args, **kwargs):
        # Caminho para salvar o backup
        backup_dir = os.path.join('core', 'cohereIA', 'resources', 'backup')
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

        # Mensagem de sucesso
        self.stdout.write(self.style.SUCCESS(f"Backup criado em {backup_file} e dados da model Dataset foram limpos."))
