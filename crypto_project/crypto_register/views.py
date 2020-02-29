from django.shortcuts import render, redirect
from .forms import CoinForm
from .models import Coin

def coin_list(request):
    context = {'coin_list': Coin.objects.all()}
    return render(request, "coin_register/coin_list.html", context)

def coin_form(request, id=0):
    if request.method == "GET":
        if id==0: #then insert operation
            form = CoinForm()
        else:
            coin = Coin.objects.get(pk=id)
            form = CoinForm(instance=coin)
        return render(request, "coin_register/coin_form.html",{'form':form})
    else:
        if id ==0:
            form = CoinForm(request.POST)
        else:
            coin = Coin.objects.get(pk=id)
            form = CoinForm(request.POST,instance=coin)
        if form.is_valid():
            form.save()
        return redirect('/coin/list')



def coin_delete(request,id):
    coin = Coin.objects.get(pk=id) 
    coin.delete()
    return redirect('/coin/list')
