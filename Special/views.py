from django.views.generic import ListView
from Special.models import SpecialMeal


class SpecialMealListView(ListView):
    model = SpecialMeal
    queryset = SpecialMeal.objects.all()
    template_name = 'index.html'