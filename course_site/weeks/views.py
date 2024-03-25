from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    return TemplateResponse(request,"weeks/home.html",)

def about(request):
    return TemplateResponse(request,"weeks/about.html",)

def contact(request):
    return TemplateResponse(request,"weeks/contact.html",)

#######################################################
#### Phys 221 Fall 2023 Site #############################
def home_modern_phys_spring_2024(request):
    return TemplateResponse(request,"weeks/home_modern_phys_spring_2024.html",)

def welcome(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/welcome.html",)

def relativity_1(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_1.html",)

def relativity_2(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_2.html",)

def relativity_3(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_3.html",)

def relativity_4(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_4.html",)

def relativity_5(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_5.html",)

def relativity_6(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_6.html",)

def relativity_7(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_7.html",)

def relativity_8(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/relativity_8.html",)

def quantum_mechanics_1(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_1.html",)

def quantum_mechanics_2(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_2.html",)

def quantum_mechanics_3(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_3.html",)

def quantum_mechanics_4(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_4.html",)

def quantum_mechanics_5(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_5.html",)

def quantum_mechanics_6(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_6.html",)

def quantum_mechanics_7(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_7.html",)

def quantum_mechanics_8(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_8.html",)

def quantum_mechanics_9(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_9.html",)

def quantum_mechanics_10(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_10.html",)

def quantum_mechanics_11(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_11.html",)

def quantum_mechanics_12(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_12.html",)

def quantum_mechanics_13(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/quantum_mechanics_13.html",)

def atoms_1(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_1.html",)

#######################################################
#### Phys 221 Fall 2023 Site #############################
def home_modern_phys(request):
    return TemplateResponse(request,"weeks/home_modern_phys.html",)

def syllabus(request):
    return TemplateResponse(request,"weeks/syllabus.html",)


def class01(request):
     return TemplateResponse( request,"weeks/class01.html",)


def class00(request):
     return TemplateResponse( request,"weeks/class00.html",)

def qm2(request):
     return TemplateResponse( request,"weeks/qm2.html",)

def expectation_values(request):
     return TemplateResponse( request,"weeks/expectation_values.html",)

def infinite_well(request):
     return TemplateResponse( request,"weeks/infinite_well.html",)

def harmonic(request):
     return TemplateResponse( request,"weeks/harmonic.html",)

def hydrogen_atom(request):
     return TemplateResponse( request,"weeks/hydrogen_atom.html",)

def exclusion(request):
     return TemplateResponse( request,"weeks/exclusion.html",)

def spin(request):
     return TemplateResponse( request,"weeks/spin.html",)

 
def multielectron(request):
     return TemplateResponse( request,"weeks/multielectron.html",)

def sr_muon(request):
     return TemplateResponse( request,"weeks/sr_muon.html",)

def vel(request):
    return TemplateResponse( request,"weeks/vel.html",)

def boltzmann(request):
    return TemplateResponse( request,"weeks/boltzmann.html",)

def simple_thermo(request):
    return TemplateResponse( request,"weeks/simple_thermo.html",)

def thermo_rec(request):
    return TemplateResponse( request,"weeks/thermo_rec.html",)

######## Up to here is Fall 2023 content ##########
###################################################
def bohr_model(request):
     return TemplateResponse( request, "weeks/bohr_model.html",)

def bound_states(request):
     return TemplateResponse( request, "weeks/bound_states.html",)

def tunneling(request):
     return TemplateResponse( request, "weeks/tunneling.html",)

def quantum_math(request):
     return TemplateResponse( request, "weeks/quantum_math.html",)

def se_3d(request):
     return TemplateResponse( request, "weeks/se_3d.html",)

def hydrogen_atom(request):
     return TemplateResponse( request, "weeks/hydrogen_atom.html",)

def hydrogen_atom2(request):
     return TemplateResponse( request, "weeks/hydrogen_atom2.html",)

def hydrogen_atom3(request):
     return TemplateResponse( request, "weeks/hydrogen_atom3.html",)

def spin(request):
     return TemplateResponse( request, "weeks/spin.html",)

def exclusion(request):
     return TemplateResponse( request, "weeks/exclusion.html",)

def multi_electron(request):
     return TemplateResponse( request, "weeks/multi_electron.html",)

def simple_thermo(request):
     return TemplateResponse( request, "weeks/simple_thermo.html",)

def boltzmann(request):
     return TemplateResponse( request, "weeks/boltzmann.html",)

def boltzmann2(request):
     return TemplateResponse( request, "weeks/boltzmann2.html",)

def maxwell(request):
     return TemplateResponse( request, "weeks/maxwell.html",)

def quantum_distros(request):
     return TemplateResponse( request, "weeks/quantum_distros.html",)

def quantum_distros2(request):
     return TemplateResponse( request, "weeks/quantum_distros2.html",)
def brownian(request):
     return TemplateResponse( request, "weeks/brownian.html",)

def photon_gas(request):
     return TemplateResponse( request, "weeks/photon_gas.html",)

def molecules1(request):
     return TemplateResponse( request, "weeks/molecules1.html",)

def molecules2(request):
     return TemplateResponse( request, "weeks/molecules2.html",)

def solids(request):
     return TemplateResponse( request, "weeks/solids.html",)

def conduction(request):
     return TemplateResponse( request, "weeks/conduction.html",)

def semiconduc(request):
     return TemplateResponse( request, "weeks/semiconduc.html",)

def superconduc(request):
     return TemplateResponse( request, "weeks/superconduc.html",)


# def simple_thermo(request):
#     if request.method == 'POST':
#         Nt = request.POST.get('textfield', None)
#         try:
#             user = Person.objects.get(name = search_id)
#             #do something with user
#             html = ("<H1>%s</H1>", user)
#             return HttpResponse(html)
#         except Person.DoesNotExist:
#             return HttpResponse("no such user")  
#     else:
#         return render(request, 'form.html')


