# frequency/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .search_frequency import start
from django.core import serializers
import json
from frequencycount.models import WordCountUrl
from frequencycount.forms import WordCountUrlForm

# Create your views here.

def index(request):
    form = WordCountUrlForm()
    wordcount = WordCountUrl.objects.all()
    return render(request, 'index.html', {"form": form, "wordcount": wordcount})

def postSearchResults(request):
    if request.method == 'POST':
        wordcount_form = WordCountUrlForm(request.POST)
        if wordcount_form.is_valid():
            user = wordcount_form.save()
            ser_user = serializers.serialize('json', [ user, ])
            return JsonResponse({"user": ser_user}, status=200)
        else:
            return JsonResponse({"error": wordcount_form.errors}, status=400)
    else:
        return JsonResponse({"error": ""}, status=400)

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