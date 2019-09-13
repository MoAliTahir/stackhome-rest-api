from django.db import models


class Apartment(models.Model):
    NUMBERS = (
        (0, 'zero'),
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
    )
    address = models.CharField(max_length=1000)
    equipped = models.BooleanField(default=False)
    bedrooms = models.IntegerField(choices=NUMBERS)
    living_room = models.IntegerField(choices=NUMBERS)
    bathroom = models.IntegerField(choices=NUMBERS, default=1)
    price = models.IntegerField(default=0)
    features = models.CharField(max_length=1000)  # fridge-gas stove-balcony-water heater-dish
    # washer-washing machine-surveillance camera-cooking tools-oven
    description = models.CharField(max_length=1000)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.address + " - " + str(self.price)
