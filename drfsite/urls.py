
from django.contrib import admin
from django.urls import path

from players.views import PlayersAPIList, PlayersAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/playerslist/',PlayersAPIList.as_view()),
    path('api/v1/playerslist/<int:pk>/',PlayersAPIList.as_view()),
]
