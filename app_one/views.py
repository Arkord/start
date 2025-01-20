from django.http import HttpResponse
from django.shortcuts import render
from app_one.models import Car, Author, Profile

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

def car_view(request, *args, **kwargs):
    print(args)
    print(kwargs)

    return HttpResponse('')

def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)

    id = kwargs['id']
    print(id)

    author = Author.objects.get(id=id);
    profile = Profile.objects.get(author_id=id)

    # print(authors)
    # print(profile)

    return HttpResponse(f"Author: {author.name} - Website: {profile.website} - Biografia: {profile.biography} ")