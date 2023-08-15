import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .utils.web_scraper import main
from .utils.gpt import gpt_response


@login_required
def index(request):
    """The home page for Study Pal."""
    return render(request, 'studypals/index.html')

@login_required
def dashboard(request):
    """The home page for Study Pal."""
    return render(request, 'studypals/dashboard.html')

@login_required
def chat(request):
    """Chat page"""
    response = None
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        query = data.get('message', '')
        # response = main(query)
        print(query)

        chat_response = gpt_response(query)
        print(chat_response)
        return JsonResponse({'response': chat_response})

        
    context = {}
    return render(request, 'studypals/chat.html', context)
