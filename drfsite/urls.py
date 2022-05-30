
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path

from players.views import PlayersViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'players', PlayersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/players/
    # path('api/v1/playerslist/',PlayersViewSet.as_view({'get': 'list'})),
    # path('api/v1/playerslist/<int:pk>/', PlayersViewSet.as_view({'put': 'update'})), 
]
