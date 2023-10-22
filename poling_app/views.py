from django.shortcuts import render, redirect
from .forms import FormImage
from .models import Images


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = FormImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = FormImage()
    img = Images.objects.all()
    return render(request, 'index.html', {'form': form, 'img': img})
