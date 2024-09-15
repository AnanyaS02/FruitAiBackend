from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.get_faqs, name='get_faqs'),
    path('faqs/<int:pk>/', views.get_faq, name='get_faq'),
    path('faqs/add/', views.add_faq, name='add_faq'),
    path('faqs/update/<int:pk>/', views.update_faq, name='update_faq'),
    path('faqs/delete/<int:pk>/', views.delete_faq, name='delete_faq'),
]
