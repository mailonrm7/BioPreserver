from django.contrib import admin
from .models import Question
from .models import Bioma

# Registro do modelo no admin
admin.site.register(Question)

# Registro do modelo Bioma no admin
admin.site.register(Bioma)

# Register your models here.
