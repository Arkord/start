from django.shortcuts import render
from app_one.models import Car

# Create your views here.
def my_view(request):
    cars = Car.objects.all()

    # car_list = [
    #     {"brand": "Honda"},
    #     {"brand": "BMW"},
    #     {"brand": "Nissan"},
    #     {"brand": "Audi"},
    #     {"brand": "Fiat"}
    # ]
    context = {
        "list": cars
    }
    return render(request, "app_one/car_list.html", context)