# frequency/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search_frequency import start
import json
from frequencycount.models import WordCountUrl
from frequencycount.forms import WordCountUrlForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term')
        if WordCountUrl.objects.filter(url=WordCountUrl.url).exists():
            print("already")
            return JsonResponse({'Search_Result': WordCountUrl.objects.get('url')})
        else:
            print("processed")
            searchResult = start(query)
            return JsonResponse({'Search_Result': searchResult})