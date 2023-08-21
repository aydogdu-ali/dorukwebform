
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FormDataMVS


router = DefaultRouter()
router.register("api",FormDataMVS )

urlpatterns = router.urls
