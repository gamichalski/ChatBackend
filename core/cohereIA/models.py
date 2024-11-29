from django.db import models

class DatasetBIAS(models.Model):
    text = models.TextField()
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class CurrentCohereIA(models.Model):
    currentModel = models.CharField(max_length=100)
    currentDataset = models.CharField(max_length=100)
    currentName = models.CharField(max_length=100)

    def __str__(self):
        return self.currentModel