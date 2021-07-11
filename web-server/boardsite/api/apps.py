from django.apps import AppConfig
from ml.model import MLModel

class ApiConfig(AppConfig):
    name = 'api'
    model = MLModel();