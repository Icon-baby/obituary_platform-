from django.shortcuts import render, redirect
from .models import Obituary
from .forms import ObituaryForm 
from django.http import HttpResponse
from django.core.paginator import Paginator 

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Obituary submitted successfully!")
    else:
        form = ObituaryForm()
    return render(request, 'submit_obituary.html', {'form': form})
    
    return render(request, 'obituaries/obituary_form.html', {'form': form})

def view_obituaries(request):
    obituary_list = Obituary.objects.all()
    paginator = Paginator(obituary_list, 10)  # Show 10 obituaries per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'obituaries/view_obituaries.html', {'page_obj': page_obj})