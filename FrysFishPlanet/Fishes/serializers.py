from rest_framework.serializers import ModelSerializer
from Fishes.models import Fish, Store


class FishSerializer(ModelSerializer):

    class Meta:
        model = Fish


class StoreSerializer(ModelSerializer):

    class Meta:
        model = Store