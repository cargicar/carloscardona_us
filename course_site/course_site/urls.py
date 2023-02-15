"""course_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from weeks.views import *  #home, class*, syllabus
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("syllabus/", syllabus, name="syllabus"),
    path("class01/", class01, name="class01"),
    path("class00/", class00, name="class00"),
    path("qm2/", qm2, name="qm2"),
    path("qm3/", qm3, name="qm3"),
    path("bohr_model/", bohr_model , name="bohr_model"),
    path("bound_states/", bound_states , name="bound_states"),
    path("tunneling/", tunneling , name="tunneling"),
    path("quantum_math/", quantum_math , name="quantum_math"),
    path("se_3d/", se_3d , name="se_3d"),
]
