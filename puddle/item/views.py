from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .form import NewItemForm
from .models import Item


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
