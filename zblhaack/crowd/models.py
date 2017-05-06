from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    ref = models.CharField(max_length=20)
    pic = models.ImageField(upload_to = 'pictures/')
    popularity = models.IntegerField(default=0)

    COLOR_CHOICE = (
        ('red', 'red'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('yellow', 'yellow'),
        ('black', 'black'),
        ('white', 'white'),
        ('grey', 'grey'),
        ('purple', 'purple'),
        ('brown', 'brown'),
        ('none', 'none'),
    )

    FAMILY_CHOICE = (
        ('t-shirt', 't-shirt'),
        ('jacket', 'jacket'),
        ('formal shoe', 'formal shoe'),
        ('sport shoe', 'sport shoe'),
        ('hat', 'hat'),
        ('pants', 'pants'),
        ('short', 'short'),
    )

    MATERIAL_CHOICE = (
        ('leather', 'leather'),
        ('cotton', 'cotton'),
        ('rubber', 'rubber'),
        ('synthetic fabric', 'synthetic fabric'),
        ('jean', 'jean'),
        ('silk', 'silk'),
    )

    BRAND_CHOICE = (
        ('brand1', 'brand1'),
        ('brand2', 'brand2'),
        ('hype brand', 'hype brand'),
        ('alf brand', 'alf brand'),
        ('annick brand', 'annick brand'),
    )

    main_color = models.CharField(max_length=10, choices=COLOR_CHOICE)
    lesser_color = models.CharField(max_length=10, choices=COLOR_CHOICE)
    family = models.CharField(max_length=11, choices=FAMILY_CHOICE)
    material = models.CharField(max_length=16, choices=MATERIAL_CHOICE)
    brand = models.CharField(max_length=16, choices=BRAND_CHOICE)
