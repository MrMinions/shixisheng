from django.contrib import admin
from .models import tImage
from .models import Text
from .models import company
class ImageInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class TextInfoAdmin(admin.ModelAdmin):
	list_display = ("name","text",)
class companyInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)
admin.site.register(tImage,ImageInfoAdmin)
admin.site.register(Text,TextInfoAdmin)
admin.site.register(company,companyInfoAdmin)