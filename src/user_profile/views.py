# coding=utf-8
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from annoying.decorators import render_to

from src.user_profile.forms import AddForm
from src.user_profile.forms import UpdateForm
from src.shop.models import Product

# вывод странички (главной) профайла
@render_to('user_profile/profiles.html')
def profile(request):
    profile_page = Product.objects.filter(user_name=request.user)
    return {"profile_vivods": profile_page}


# вывод странички после добавления записи
@render_to('user_profile/done.html')
def done(request):
    thx = 'спасибо за добавление'
    return {"thx": thx}


# добавление лота
@render_to('user_profile/addform.html')
def addform(request):
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.image = form.cleaned_data['image']
            add.user_name_id = request.user
            add.save()
            return redirect('src.user_profile.views.done')
    else:
        form = AddForm()
    return {'form': form}


@render_to('user_profile/redaktor.html')
def redaktor(request, product_id=1):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.user_name = request.user
            update.save()
            return redirect('src.user_profile.views.done')
    else:
        form = UpdateForm()
    return {'product': product, 'update_form': form}


# Удаление продукта
@render_to('shop/index.html')
def product_delete(request, product_id):
    d = get_object_or_404(Product, pk=product_id)
    product_del = d.descp
    d.delete()
    return {'product_del': product_del}
