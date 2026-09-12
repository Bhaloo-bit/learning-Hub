from django.urls import path
from . import views
urlpatterns = [
    path('singleobj/', views.singleobj),
    path('multipleobj/', views.multipleobj),

]
