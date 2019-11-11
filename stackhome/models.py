from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from multiselectfield import MultiSelectField


DISTRICTS = (
        ("M'hannech","M'hannech"), ("Touta","Touta"), ("Martil","Martil"), ("Wilaya","Wilaya"),
        ("Saniat Rmel","Saniat Rmel"), ("Safir","Safir"),("Soukna w Ta3mir","Soukna w Ta3mir"),
        ("Autre","Autre")
)
NUMBERS = (
    (0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),
)


class UserManager(BaseUserManager):
    def create_user(self, email, id_card, phone_number, full_name, password=None, is_staff=False, is_admin=False,
                    image="default.jpg"):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not id_card:
            raise ValueError('Users must have an ID card')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not full_name:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.id_card = id_card
        user.phone_number = phone_number
        user.full_name = full_name
        user.staff = is_staff
        user.admin = is_admin
        user.image = image
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, id_card, phone_number, full_name, password, image="default.jpg"):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email=email,
            id_card=id_card,
            phone_number=phone_number,
            full_name=full_name,
            is_staff=True,
            password=password,
            image=image,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, id_card, phone_number, full_name, password, image="default.jpg"):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            id_card=id_card,
            phone_number=phone_number,
            full_name=full_name,
            is_staff=True,
            is_admin=True,
            password=password,
            image=image,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    id_card = models.IntegerField()
    phone_number = models.IntegerField()
    full_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id_card', 'phone_number', 'full_name']  # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active


class Apartment(models.Model):
    FEATURES = (
        ("Fridge", "Fridge"), ("Gas stove", "Gas stove"), ("Balcony", "Balcony"), ("Water heater", "Water heater"),
        ("Dish washer", "Dish washer"), ("Washing machine", "Washing machine"), ("television", "television"),
        ("Surveillance camera", "Surveillance camera"), ("Cooking tools", "Cooking tools"), ("Oven", "Oven"),
        ("Wifi", "Wifi"),
    )
    owner = models.ForeignKey(User, related_name='apartments', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    district = models.CharField(max_length=20, choices=DISTRICTS)
    equipped = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    bedrooms = models.IntegerField(choices=NUMBERS)
    living_room = models.IntegerField(choices=NUMBERS)
    bathroom = models.IntegerField(choices=NUMBERS, default=1)
    price = models.IntegerField(default=0)
    features = MultiSelectField(choices=FEATURES)  # fridge-gas stove-balcony-water heater-dish
    # washer-washing machine-surveillance camera-cooking tools-oven
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    img1 = models.FileField(upload_to='apartment_pics', blank=True)
    img2 = models.FileField(upload_to='apartment_pics', blank=True)
    img3 = models.FileField(upload_to='apartment_pics', blank=True)
    img4 = models.FileField(upload_to='apartment_pics', blank=True)
    img5 = models.FileField(upload_to='apartment_pics', blank=True)
    img6 = models.FileField(upload_to='apartment_pics', blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.address + " - " + str(self.price)


class Room(models.Model):
    FEATURES = (
        ("Fridge", "Fridge"), ("Desk", "Desk"), ("Balcony", "Balcony"),
        ("Cabinet", "Cabinet"), ("Attached bath", "Attached bath"),
    )
    owner = models.ForeignKey(User, related_name='rooms', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    district = models.CharField(max_length=20, choices=DISTRICTS)
    equipped = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    price = models.IntegerField()
    beds = models.IntegerField(choices=NUMBERS)
    features = MultiSelectField(choices=FEATURES, blank=True)  # fridge-gas stove-balcony-water heater-dish
    # washer-washing machine-surveillance camera-cooking tools-oven
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    img1 = models.FileField(upload_to='apartment_pics', blank=True)
    img2 = models.FileField(upload_to='apartment_pics', blank=True)
    img3 = models.FileField(upload_to='apartment_pics', blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.address + " - " + str(self.price)


class Rent(models.Model):
    STATE = (
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Ignored'),
    )
    tenant = models.ForeignKey(User, related_name='rents', on_delete=models.DO_NOTHING)
    apartment = models.ForeignKey(Apartment, related_name='rents', on_delete=models.DO_NOTHING, null=True)
    room = models.ForeignKey(Room, related_name='rents', on_delete=models.DO_NOTHING, null=True)
    state = models.IntegerField(choices=STATE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.tenant.full_name + " - state : " + str(self.state)