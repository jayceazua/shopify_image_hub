from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from django.utils import timezone
from django.db.models import Q


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

# UPDATE
@login_required(login_url="/accounts/signup")
def update(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    pass


def filter_results(results, current_item_id):
    """
        Handles duplicate results when getting related images
    """
    filtered_results = []
    seen = set()
    seen.add(current_item_id)

    for result in results:
        for item in result:
            if item.id not in seen:
                filtered_results.append(item)
                seen.add(item.id)
    return filtered_results

# READ
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # query
    results = []
    queries = item.caption.split(" ")
    for query in queries:
        itms = Item.objects.filter(Q(caption__icontains=query) | Q(description__icontains=query))
        results = results + [itms]

    items = filter_results(results, item_id)
    return render(request, 'item/detail.html', {'item': item, 'items': items})

# DELETE
@login_required(login_url="/accounts/signup")
def delete(request, item_id):
    # fetch the object related to passed id
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        # delete object
        item.delete()
    return redirect('/')

# SEARCH
def search(request):
    template_name = 'item/home.html'
    query = request.GET.get('q')
    results = Item.objects.filter(Q(caption__icontains=query) | Q(description__icontains=query))
    return render(request, template_name, {'items': results})
