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
    
    ############ Current 2023 content #######################
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
