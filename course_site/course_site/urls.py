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

    ############ phys 221 Fall 2023 ##############################
    path("syllabus/", syllabus, name="syllabus"),
    path("home_modern_phys/",home_modern_phys, name="home_modern_phys"),
    path("class01/", class01, name="class01"),
    path("class00/", class00, name="class00"),
    path("qm2/", qm2, name="qm2"),
    path("expectation_values/", expectation_values, name="expectation_values"),
    path("infinite_well/", infinite_well, name="infinite_well"),
    path("harmonic/", harmonic, name="harmonic"),
    path("hydrogen_atom/", hydrogen_atom, name="hydrogen_atom"),
    path("exclusion/", exclusion, name="exclusion"),
    path("spin/", spin, name="spin"),
    path("multielectron/", multielectron, name="multielectron"),
    path("sr_muon/", sr_muon, name="sr_muon"),
    path("vel/", vel, name="vel"),
    path("boltzmann/", boltzmann, name="boltzmann"),
    path("simple_thermo/", simple_thermo, name="simple_thermo"),
    path("thermo_rec/", thermo_rec, name="thermo-rec"),
    
    #########################################
    path("bohr_model/", bohr_model , name="bohr_model"),
    path("bound_states/", bound_states , name="bound_states"),
    path("tunneling/", tunneling , name="tunneling"),
    path("quantum_math/", quantum_math , name="quantum_math"),
    path("se_3d/", se_3d , name="se_3d"),
    path("hydrogen_atom/", hydrogen_atom , name="hydrogen_atom"),
    path("hydrogen_atom2/", hydrogen_atom2 , name="hydrogen_atom2"),
    path("hydrogen_atom3/", hydrogen_atom3 , name="hydrogen_atom3"),
    path("spin/", spin , name="spin"),
    path("exclusion/", exclusion , name="exclusion"),
    path("multi_electron/",  multi_electron, name="multi_electron"),
    path("simple_thermo/",  simple_thermo, name="simple_thermo"),
    path("boltzmann/",  boltzmann, name="boltzmann"),
    path("boltzmann2/",  boltzmann2, name="boltzmann2"),
    path("maxwell/",  maxwell, name="maxwell"),
    path("quantum_distros/",  quantum_distros, name="quantum_distros"),
    path("quantum_distros2/",  quantum_distros2, name="quantum_distros2"),
    path("brownian/", brownian, name="brownian"),
    path("photon_gas/", photon_gas, name="photon_gas"),
    path("molecules1/", molecules1, name="molecules1"),
    path("molecules2/", molecules2, name="molecules2"),
    path("solids/", solids, name="solids"),
    path("conduction/", conduction, name="conduction"),
    path("semiconduc/", semiconduc, name="semiconduc"),
    path("superconduc/", superconduc, name="superconduc"),
]
