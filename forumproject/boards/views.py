from django.http import HttpResponse
from django.shortcuts import render
from .models import Board


def home(request):
    boards = Board.objects.all()

    return render(request, 'index.html', {'boards': boards})

