from django.urls import path
from Special.views import SpecialMealListView

urlpatterns = [
    path(" ", SpecialMealListView.as_view(), name='special'),
]