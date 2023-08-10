<<<<<<< HEAD
from django.shortcuts import render

from .models import Text
from .forms import TextForm

from .utilities.web_scraper import main

# Create your views here.
def index(request):
    """The home page for Study Pal."""
    return render(request, 'studypals/index.html')

def dashboard(request):
    """The home page for Study Pal."""
    return render(request, 'studypals/dashboard.html')

def chat(request):
    """Chat page"""
    response = None
    if request.method == 'POST':
        prompt = request.POST.get('user_input')
        response = main(prompt)

        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TextForm()
        
    context = {'response': response, 'form': form}
    return render(request, 'studypals/chat.html', context)
=======
from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'studypals/index.html')
>>>>>>> 8370b914406d0e7e6cc81cdd76708d4004b83da8