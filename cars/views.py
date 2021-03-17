from django.shortcuts import render, get_object_or_404

# Create your views here.
from cars.models import Car


def cars(request):
  cars = Car.objects.order_by('-created_date')
  context = {
    'cars': cars
  }
  return render(request, 'cars/cars.html', context)


def car_detail(request, id):
  single_car = get_object_or_404(Car, pk=id)
  context = {
    'single_car': single_car
  }
  return render(request, 'cars/car_detail.html', context)