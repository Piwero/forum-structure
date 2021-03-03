from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board


def home(request):
    boards = Board.objects.all()

    return render(request, 'index.html', {'boards': boards})


def board_topics(request, pk):
    try:
        board = get_object_or_404(Board, pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})