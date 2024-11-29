from rest_framework.serializers import ModelSerializer
from core.cohereIA.models import DatasetBIAS, CurrentCohereIA

class DatasetBIASSerializer(ModelSerializer):
    class Meta:
        model = DatasetBIAS
        fields = ["text", "label"]


class CurrentCohereIASerializer(ModelSerializer):
    
    class Meta:
        model = CurrentCohereIA
        fields = ["currentModel", "currentDataset", "currentName"]
