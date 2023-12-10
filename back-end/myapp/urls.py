from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import UserView

router = routers.DefaultRouter()
router.register(r'users', UserView, 'users')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title = 'Project API'))
]