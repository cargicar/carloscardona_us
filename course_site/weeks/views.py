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

##################### Talsk ##########################
def talk_10(request):
    return TemplateResponse(request,"weeks/talk_10.html",)

def pizza_cerca(request):
    return TemplateResponse(request,"weeks/pizza_cerca.html",)


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

def atoms_2(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_2.html",)

def atoms_3(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_3.html",)

def atoms_4(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_4.html",)

def atoms_5(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_5.html",)

def atoms_6(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_6.html",)

def atoms_7(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_7.html",)

def atoms_8(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_8.html",)

def atoms_9(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/atoms_9.html",)

def sm_1(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/sm_1.html",)

def sm_2(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/sm_2.html",)

def sm_3(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/sm_3.html",)

def sm_4(request):
    return TemplateResponse(request,"weeks/phys221_spring2024/sm_4.html",)

#######################################################
#### Phys 221 Fall 2023 Site #############################
def home_modern_phys(request):
    return TemplateResponse(request,"weeks/home_modern_phys.html",)


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


