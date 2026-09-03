from django.contrib import admin
from .models import ChaiVarity, ChaiReview, ChaiCertificate,Store

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model= ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display =('name','type','date_added')     


admin.site.register(ChaiVarity)

