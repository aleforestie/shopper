from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    ref = models.CharField(max_length=20)
    pic = models.ImageField(upload_to = 'crowd/static/crowd/images/')
    popularity = models.IntegerField(default=0)

    COLOR_CHOICE = (
        ('red', 'red'),
        ('blue', 'blue'),
        ('black', 'black'),
        ('white', 'white'),
    )

    FAMILY_CHOICE = (
        ('t-shirt', 't-shirt'),
        ('jacket', 'jacket'),
        ('sport shoe', 'sport shoe'),
        ('pants', 'pants'),
    )

    MATERIAL_CHOICE = (
        ('leather', 'leather'),
        ('cotton', 'cotton'),
        ('synthetic fabric', 'synthetic fabric'),
        ('jean', 'jean'),
    )

    BRAND_CHOICE = (
        ('hype brand', 'hype brand'),
        ('alf brand', 'alf brand'),
        ('annick brand', 'annick brand'),
    )

    main_color = models.CharField(max_length=10, choices=COLOR_CHOICE)
    lesser_color = models.CharField(max_length=10, choices=COLOR_CHOICE)
    family = models.CharField(max_length=11, choices=FAMILY_CHOICE)
    material = models.CharField(max_length=16, choices=MATERIAL_CHOICE)
    brand = models.CharField(max_length=16, choices=BRAND_CHOICE)

class FavoriteColor(models.Model):
    red = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)
    black = models.IntegerField(default=0)
    white = models.IntegerField(default=0)

class FavoriteBrand(models.Model):
    hype_brand = models.IntegerField(default=0)
    alf_brand = models.IntegerField(default=0)
    annick_brand = models.IntegerField(default=0)

class FavoriteFamily(models.Model):
    t_shirt = models.IntegerField(default=0)
    jacket = models.IntegerField(default=0)
    sport_shoe = models.IntegerField(default=0)
    pants = models.IntegerField(default=0)
