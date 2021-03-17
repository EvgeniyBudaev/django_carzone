from ckeditor.fields import RichTextField
from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField


# Create your models here.


class Car(models.Model):
  state_choice = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
  )

  year_choice = []
  for r in range(2000, (datetime.now().year+1)):
    year_choice.append((r, r))

  features_choices = (
    ('Cruise Control', 'Cruise Control'),
    ('Audio Interface', 'Audio Interface'),
    ('Airbags', 'Airbags'),
    ('Air Conditioning', 'Air Conditioning'),
    ('Seat Heating', 'Seat Heating'),
  )

  doors_choices = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
  )

  car_title = models.CharField(max_length=255)
  state = models.CharField(max_length=255, choices=state_choice)
  city = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  year = models.IntegerField(('year'), choices=year_choice)
  condition = models.CharField(max_length=100)
  price = models.IntegerField()
  description = RichTextField()
  car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  car_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  features = MultiSelectField(choices=features_choices)
  body_style = models.CharField(max_length=100)
  engine = models.CharField(max_length=100)
  transmission = models.CharField(max_length=100)
  interior = models.CharField(max_length=100)
  miles = models.IntegerField()
  doors = models.CharField(max_length=10, choices=doors_choices)
  passengers = models.IntegerField()
  vin_no = models.CharField(max_length=100)
  milage = models.IntegerField()
  fuel_type = models.CharField(max_length=50)
  no_of_owners = models.CharField(max_length=100)
  is_featured = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=datetime.now, blank=True)

