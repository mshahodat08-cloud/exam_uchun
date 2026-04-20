from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # 🏠 ASOSIY
    path('', views.asosiy, name='home'),

    # 📋 TALABALAR
    path('list/', views.talabalar_royxati, name='list'),
    path('qoshish/', views.talaba_qoshish, name='add'),

    path('<int:pk>/tahrirlash/', views.talaba_tahrirlash, name='edit'),
    path('<int:pk>/ochirish/', views.talaba_ochirish, name='delete'),
    path('<int:pk>/', views.talaba_detail, name='detail'),

    # 👥 GURUH
    path('guruhlar/', views.guruhlar_royxati, name='guruhlar'),
    path('guruhlar/qoshish/', views.guruh_qoshish, name='guruh_add'),
    path('guruhlar/<int:pk>/tahrirlash/', views.guruh_tahrirlash, name='guruh_edit'),
    path('guruhlar/<int:pk>/ochirish/', views.guruh_ochirish, name='guruh_delete'),
]