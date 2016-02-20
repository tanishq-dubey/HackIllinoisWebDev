from Fishes import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'fish', views.FishViewSet)
router.register(r'stores', views.StoreViewSet)

urlpatterns = router.urls