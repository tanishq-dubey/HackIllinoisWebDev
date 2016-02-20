from django.shortcuts import render, get_object_or_404
from Fishes.models import Fish, Store

from rest_framework.viewsets import ModelViewSet
from Fishes.serializers import FishSerializer, StoreSerializer


# Create your views here.

def index(request):
	fishes = Fish.objects.all()
	stores = Store.objects.order_by("-location").reverse()
	return render(request, 'Fishes/index.html', {"fishes": fishes, "stores": stores})

def detail(request, store_id):
	stores = get_object_or_404(Store, pk=store_id)
	return render(request, 'Fishes/detail.html', {"stores": stores})

class FishViewSet(ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer