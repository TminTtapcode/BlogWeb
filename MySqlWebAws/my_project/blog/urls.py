from django.urls import path
from . import views  # Import các view từ thư mục hiện tại

urlpatterns = [
    # Khi người dùng truy cập /blog/, nó sẽ gọi hàm 'post_list'
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_create, name='post_create'),
    path('<int:pk>/edit/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
]