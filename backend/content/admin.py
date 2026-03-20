from django.contrib import admin
from .models import (
    Location,
    Category,
    Experience,
    PricingRule,
    OperatingHours,
)

myModels = [Location,Category, Experience, PricingRule, OperatingHours]

admin.site.register(myModels)
