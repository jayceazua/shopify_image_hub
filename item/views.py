from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from django.utils import timezone


def home(request):
    items = Item.objects
    return render(request, 'item/home.html', {'items': items})

# CREATE
@login_required(login_url="/accounts/signup")
def add(request):
    if request.method == 'POST':
        if request.POST['caption'] and request.FILES['icon'] and request.FILES['image'] and request.POST['description']:

            item = Item()
            item.caption = request.POST['caption']
            item.icon = request.FILES['icon']
            item.image = request.FILES['image']
            item.artist = request.user
            item.description = request.POST['description']

            item.save()

            return redirect('/item/' + str(item.id))

        else:
            return render(request, 'item/add.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'item/add.html')

# READ
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item/detail.html', {'item': item})

# UPDATE
@login_required(login_url="/accounts/signup")
def update(request, item_id):
    pass

# DELETE
@login_required(login_url="/accounts/signup")
def delete(request, item_id):
    # fetch the object related to passed id
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        # delete object
        item.delete()
    return redirect('/')
