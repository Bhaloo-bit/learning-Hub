from django.urls import path
from . import views

urlpatterns = [
    path('',views.books, name='books'),
    path('<int:chai_id>/',views.chai_detail, name='chai_details'),
    
]

