from django.shortcuts import render
from .models import mytest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.http import HttpResponse
from llm import LLMChain
from rest_framework.response import Response
from datetime import datetime


def index(request):
    return HttpResponse('ITS Running')


@csrf_exempt
@api_view(['POST', 'GET'])
def add_test(request):
    if request.method == 'POST':
        data = request.data
        llm_text = data.get('LLM')
        text_data = data.get('text')

        res1 = LLMChain(llm_text, text_data)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            'Time_Initiated': timestamp,
            'LLM_type': llm_text,
            'input_text': text_data,
            'AI_text': res1
        }
        data1 = []
        for i in data:
            data1.append(data[i])
        modeldb = mytest(val1 = llm_text,val2=text_data,val3=res1)
        modeldb.save()
        return JsonResponse({'data1': data1}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

