from django.shortcuts import render

# Create your views here.
from board.models import Board

def list(request):
    board = Board.objects.all().order_by('-reg_date')
    data = {'board': board}
    for t in board:
        print(t)
    return render(request, 'board/list.html',data)