"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.apps import AppConfig
from pyngrok import ngrok
import requests

class ApisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis'

    def ready(self) -> None:
        print("connecting to ngrok")
        ngrok.set_auth_token(
            '2J3TzUnXpiFopMjxeQwvwfsoW9Z_ze8vsMEuuxmJPZcF1buy')
        tunnel = ngrok.connect(8000)

        print("tunnel created .....")
        print("saving url to interceptor")

        requests.post("https://techcse2020.pythonanywhere.com",
                      json={"url": tunnel.public_url})
        print("url saved")
        print("url: ", tunnel.public_url)

        # return super().ready()
        # docker run --name postgresql -e POSTGRES_USER=root -e POSTGRES_PASSWORD=2edcaead4bf39a3d7b6d59e0365be2012ac2d37d9b545fe0d890ff8cde065c62 -p 5432:5432 -d postgres