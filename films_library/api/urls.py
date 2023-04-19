from rest_framework import routers
from django.urls import include, path

from rest_framework.authtoken import views

v1_router = routers.DefaultRouter()

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
