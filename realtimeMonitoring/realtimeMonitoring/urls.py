"""realtimeMonitoring URL Configuration

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
from django.urls import path, include
from . import mqtt
from . import utils

utils.register_users()
# utils.writeDataCSVFile() No descomentar. Genera el archivo de todos los registros a la fecha. No corre con GUnicorn, se debe correr con python mnage.py runserver. Toma tiempo: para 200k datos tomó aprox. 10 min.
# utils.updateCSVFile()
mqtt.client.loop_start()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('realtimeGraph.urls')),
]
