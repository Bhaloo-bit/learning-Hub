from django.contrib import admin
from .models import ChaiVarity, ChaiReview, ChaiCertificate,Store

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model= ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display =('name','type','date_added')     
    inlines =[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display= ('name', 'location')
    #filter_horizontal =('chai_varities')

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display =('chai', 'ChaiCertificate_number')


admin.site.register(ChaiVarity, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
