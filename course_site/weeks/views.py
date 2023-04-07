from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    return TemplateResponse(request,"weeks/home.html",)
    #return (request, 'homeApp/home.html')

def syllabus(request):
    return TemplateResponse(request,"weeks/syllabus.html",)


def class01(request):
     return TemplateResponse( request,"weeks/class01.html",)


def class00(request):
     return TemplateResponse( request,"weeks/class00.html",)

def qm2(request):
     return TemplateResponse( request,"weeks/qm2.html",)

def qm3(request):
     return TemplateResponse( request,"weeks/qm3.html",)


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


