# frequency/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search_frequency import start
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term')
        searchResult = start(query)
        return JsonResponse({'Search_Result': searchResult})
        #if query:
         #   searchResult = start(query)
          #  if len(searchResult) == 0:
           #     return JsonResponse({'Search_Result': "Word not found."})
            #else:
             #   return JsonResponse({'Search_Result': searchResult})
        #else:
         #   return redirect('/')