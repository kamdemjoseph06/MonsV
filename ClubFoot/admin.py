from django.contrib import admin

# Register your models here.
from django.contrib import admin
#from .models import inscription,imgVid
from ClubFoot.models import inscription,imgVidUser,img,Vid,Infomedia,Doc

@admin.register(inscription)
class inscriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(imgVidUser)
class imgVid(admin.ModelAdmin):
    pass

@admin.register(img)
class img(admin.ModelAdmin):
    list_display = ('titre', 'image_choisie')

@admin.register(Vid)
class Vid(admin.ModelAdmin):
    list_display = ('titre', 'video_choisie')

@admin.register(Infomedia)
class Infomedia(admin.ModelAdmin):
    pass

@admin.register(Doc)
class Doc(admin.ModelAdmin):
    pass