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
from weeks.views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),

    ############## Talks #############################
    path("talk_10/", talk_10, name="talk_10"),
    path("pizza_cerca/", pizza_cerca, name="pizza_cerca"),
    ############ phys 221 Spring 2024 ##############################
    #path("syllabus/", syllabus, name="syllabus"),
    path("home_modern_phys_spring_2024/",home_modern_phys_spring_2024, name="home_modern_phys_spring_2024"),
    path("phys221_spring2024/welcome/", welcome, name="welcome"),
    path("phys221_spring2024/relativity_1/", relativity_1, name="relativity_1"),
    path("phys221_spring2024/relativity_2/", relativity_2, name="relativity_2"),
    path("phys221_spring2024/relativity_3/", relativity_3, name="relativity_3"),
    path("phys221_spring2024/relativity_4/", relativity_4, name="relativity_4"),
    path("phys221_spring2024/relativity_5/", relativity_5, name="relativity_5"),
    path("phys221_spring2024/relativity_6/", relativity_6, name="relativity_6"),
    path("phys221_spring2024/relativity_7/", relativity_7, name="relativity_7"),
    path("phys221_spring2024/relativity_8/", relativity_8, name="relativity_8"),
    path("phys221_spring2024/quantum_mechanics_1/", quantum_mechanics_1 , name="quantum_mechanics_1"),
    path("phys221_spring2024/quantum_mechanics_2/", quantum_mechanics_2 , name="quantum_mechanics_2"),
    path("phys221_spring2024/quantum_mechanics_3/", quantum_mechanics_3 , name="quantum_mechanics_3"),
    path("phys221_spring2024/quantum_mechanics_4/", quantum_mechanics_4 , name="quantum_mechanics_4"),
    path("phys221_spring2024/quantum_mechanics_5/", quantum_mechanics_5 , name="quantum_mechanics_5"),
    path("phys221_spring2024/quantum_mechanics_6/", quantum_mechanics_6 , name="quantum_mechanics_6"),
    path("phys221_spring2024/quantum_mechanics_7/", quantum_mechanics_7 , name="quantum_mechanics_7"),
    path("phys221_spring2024/quantum_mechanics_8/", quantum_mechanics_8 , name="quantum_mechanics_8"),
    path("phys221_spring2024/quantum_mechanics_9/", quantum_mechanics_9 , name="quantum_mechanics_9"),
    path("phys221_spring2024/quantum_mechanics_10/", quantum_mechanics_10 , name="quantum_mechanics_10"),
    path("phys221_spring2024/quantum_mechanics_11/", quantum_mechanics_11 , name="quantum_mechanics_11"),
    path("phys221_spring2024/quantum_mechanics_12/", quantum_mechanics_12 , name="quantum_mechanics_12"),
    path("phys221_spring2024/quantum_mechanics_13/", quantum_mechanics_13 , name="quantum_mechanics_13"),
    path("phys221_spring2024/atoms_1/", atoms_1, name="atoms_1"),
    path("phys221_spring2024/atoms_2/", atoms_2, name="atoms_2"),
    path("phys221_spring2024/atoms_3/", atoms_3, name="atoms_3"),
    path("phys221_spring2024/atoms_4/", atoms_4, name="atoms_4"),
    path("phys221_spring2024/atoms_5/", atoms_5, name="atoms_5"),
    path("phys221_spring2024/atoms_6/", atoms_6, name="atoms_6"),
    path("phys221_spring2024/atoms_7/", atoms_7, name="atoms_7"),
    path("phys221_spring2024/atoms_8/", atoms_8, name="atoms_8"),
    path("phys221_spring2024/atoms_9/", atoms_9, name="atoms_9"),
    path("phys221_spring2024/sm_1/", sm_1, name="sm_1"),
    path("phys221_spring2024/sm_2/", sm_2, name="sm_2"),
    path("phys221_spring2024/sm_3/", sm_3, name="sm_3"),
    path("phys221_spring2024/sm_4/", sm_4, name="sm_4"),
    path("phys221_spring2024/sm_5/", sm_5, name="sm_5"),
]
