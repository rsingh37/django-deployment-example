from django.shortcuts import render
import random
import string

def generate_password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        return render(request, 'generator/result.html', {'password': password})
    return render(request, 'generator/home.html')
