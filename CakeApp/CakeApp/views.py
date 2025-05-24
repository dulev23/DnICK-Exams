from django.shortcuts import render, redirect

from .forms import CakeForm
from .models import Cake, Baker


# Create your views here.

def index(request):
    cakes = Cake.objects.all()
    context = {'cakes': cakes, 'app_name': 'CakeApp'}
    return render(request, 'index.html', context)


def add(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.baker = Baker.objects.filter(user=request.user).first()
            cake.save()
        return redirect('index')
    form = CakeForm()
    return render(request, 'add.html', context={'form': form})
