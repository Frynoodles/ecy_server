from django.urls import path
from api.views import bili_info

urlpatterns = [
    path('info',api.views.bili_info ),
]
