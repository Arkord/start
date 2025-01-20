"""
URL configuration for project_one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.http import HttpRequest, HttpResponse
from django.urls import path
from app_one.views import car_view, author_view

# def my_view(request):
#     return ''

# def my_view(request, *args, **kwargs):
#     print(args)
#     print(kwargs)

#     return HttpResponse('')

# urlpatterns = [
#     path('list/', my_view),
#     path('detail/<int:id>', my_view),
#     path('brands/<str:brand>', my_view)
# ]

urlpatterns = [
    path('list/', car_view),
    path('detail/<int:id>', car_view),
    path('brands/<str:brand>', car_view),
    path('authors/', author_view),
    path('authors/<int:id>', author_view)
]