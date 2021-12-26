from django.shortcuts import render

def index(request):
    return render(request, 'enterprises/parts/01_index.html')

def inperiodical(request):
    return render(request, 'enterprises/parts/04_1_inperiodical.html')

def addperiodical(request):
    return render(request, 'enterprises/parts/04_2_addperiodical.html')