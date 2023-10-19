from django.shortcuts import render

def introduction(request,):
    return render(request, 'introduction/introduction.html', {})

def lets_start_personalizing(request,):
    return render(request, 'introduction/lets-start-personalizing.html', {})
