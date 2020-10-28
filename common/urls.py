from django.urls import path
from common.views import login_view, index

urlpatterns = [
    path('login', login_view, name="login"),
    path('index', index, name="index")
]