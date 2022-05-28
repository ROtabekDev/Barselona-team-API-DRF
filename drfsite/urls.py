
from django.contrib import admin
from django.urls import path

from players.views import PlayersAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/playerslist/',PlayersAPIView.as_view()),
    path('api/v1/playerslist/<int:pk>/',PlayersAPIView.as_view()),
]
