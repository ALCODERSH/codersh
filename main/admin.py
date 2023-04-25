from django.contrib import admin
from .models import Language, AceTheme, AceFont
# Register your models here.
admin.site.register(Language)
admin.site.register(AceTheme)
admin.site.register(AceFont)