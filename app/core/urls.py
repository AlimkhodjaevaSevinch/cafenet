from django.urls import path
from app.core.views import MainPageView


urlpatterns = [
    path('', MainPageView.as_view())
]
