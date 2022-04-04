import django


from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import Familia

def familia_lista(request):

   familia= Familia.objects.all()

   context= {'familia:': familia}
   
   return HttpResponse(request, 'familia_lista.html', context)


   