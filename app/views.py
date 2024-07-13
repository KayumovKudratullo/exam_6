from django.shortcuts import render, redirect
from . import models

# Create your views here.
def main(request):
    banner = models.Banner.objects.last()
    special = models.Meals.objects.last()
    appetiser = models.Meals.objects.filter(category = 3).values()
    main_food= models.Meals.objects.filter(category = 1).values()
    salad = models.Meals.objects.filter(category = 2).values()
    chef = models.AboutUs.objects.last()
    comments = models.Comment.objects.all()
    context = {
        'banner': banner,
        'special': special,
        'main_foods': main_food,
        'appetisers': appetiser,
        'salads': salad,
        'chef': chef,
        'comments': comments,
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
    main = models.Meals.objects.get(id=id)
    print(main.cook.full_name)
    context = {
        'main': main,}
    return render(request, 'test.html', context,)