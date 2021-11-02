from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import StockItem


# Create your views here.


def todoView(request):
    items = StockItem.objects.all()
    return render(request,'todo.html', {'items' : items})





def addTodo(request):
    # create a new item 
    # save
    # redirect the browser to '/todo/'
    new_item= StockItem(date=request.POST['date'], 
        trans=request.POST['trans'], symbol=request.POST['symbol'], 
        qty=request.POST['qty'], price=request.POST['price']) 
    new_item.save()
    return HttpResponseRedirect('/todo/')