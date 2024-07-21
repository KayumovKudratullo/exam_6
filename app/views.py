from django.shortcuts import render, redirect
from . import models
from Special.models import SpecialMeal
from random import shuffle

# Create your views here.
def main(request):
    banner = models.Banner.objects.last()
    special = models.Meal.objects.last()
    appetiser = models.Meal.objects.filter(category = 3).values()
    main_food= models.Meal.objects.filter(category = 1).values()
    salad = models.Meal.objects.filter(category = 2).values()
    chef = models.AboutUs.objects.last()
    comments = models.Comment.objects.all()
    queryset = SpecialMeal.objects.all()
    q = shuffle(list(queryset) + list(salad))
    context = {
        'banner': banner,
        'special': special,
        'main_foods': main_food,
        'appetisers': appetiser,
        'salads': salad,
        'chef': chef,
        'comments': comments,
        'queryset':q,
    }

    if request.method == 'POST':
        message = request.POST['message']
        models.Comment.objects.create(
            author=request.user,
            body=message,
        )
        
    return render(request, 'index.html', context)

def corusel(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        party = request.POST['party']

        models.Reserve.objects.create(
            full_name = name,
            email = email,
            date = date, 
            party = party
        )
    return render(request, 'corusel.html')


def test(request, id):
    main = models.Meal.objects.get(id=id)
    print(main.cook.full_name)
    context = {
        'main': main,}
    return render(request, 'test.html', context,)