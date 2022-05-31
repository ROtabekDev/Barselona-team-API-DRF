

from django.contrib import admin
from django.urls import path, include

from players.views import PlayersViewSet
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                mapping={'get': 'list'},
                name='{basename}-list',
                detail=False,
                initkwargs={'suffix': 'List'}),

        routers.Route(url=r'^{prefix}/{lookup}$',
                mapping={'get': 'retrieve'},
                name='{basename}-detail',
                detail=True,
                initkwargs={'suffix': 'Detail'}),

    ]

router = MyCustomRouter()
router.register(r'players', PlayersViewSet, basename='players')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/players/
    # path('api/v1/playerslist/',PlayersViewSet.as_view({'get': 'list'})),
    # path('api/v1/playerslist/<int:pk>/', PlayersViewSet.as_view({'put': 'update'})), 
]
