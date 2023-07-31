from django.urls import path, include

from ecommerce.core.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home page'),
]
