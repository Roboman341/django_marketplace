from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .forms import NewItemForm, EditItemForm
from .models import Category, Item


def items(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )  # performs a case-insensitive search

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "query": query,
            "categories": categories,
            "category_id": int(category_id),
        },
    )


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        category=item.category,
        is_sold=False).exclude(
        pk=pk)[
            0:3]

    return render(request, "item/detail.html",
                  {"item": item, "related_items": related_items})


@login_required
def new(
    request,
):  # if the user was about to hit this view without being authenticated - it'll be redirected to the log in page
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # if we try to save to db now the created_by field is not added and
            # we'll get an error. We create an object but not save it
            item = form.save(commit=False)
            # user is always authenticated because we have @login_required
            # decorator
            item.created_by = request.user
            item.save()

            return redirect(
                "item:detail", pk=item.id
            )  # this primary key = id of the item we've created
    else:
        form = NewItemForm()
    return render(request, "item/form.html",
                  {"form": form, "title": "New item"})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")


@login_required
def edit(request, pk):  # need primary key to get the correct item from the database
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()  # created_by is set so we can just save the form

            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, "item/form.html",
                  {"form": form, "title": "Edit item"})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")
