from django.urls import path
from . import views

urlpatterns = [
    path('', views.body_list, name='body_list'),
    path('add/', views.body_add, name='body_add'),
    path('<int:pk>/edit/', views.body_edit, name='body_edit'),
    path('<int:pk>/delete/', views.body_delete, name='body_delete'),
    path('accounts/signup/', views.signup, name='signup'),  # 新規登録ページの追加
]
