from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404


from cars.models import Car

# Create your views here.


def cars(request):
  cars = Car.objects.order_by('-created_date')
  paginator = Paginator(cars, 4)
  page = request.GET.get('page')
  paged_cars = paginator.get_page(page)
  context = {
    'cars': paged_cars,
  }
  return render(request, 'cars/cars.html', context)


def car_detail(request, id):
  single_car = get_object_or_404(Car, pk=id)
  context = {
    'single_car': single_car
  }
  return render(request, 'cars/car_detail.html', context)