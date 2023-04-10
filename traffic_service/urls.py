from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('customer/', views.customer, name='customer'),

    # ...
    path('login/', auth_views.LoginView.as_view(template_name='custom_login.html'), name='login'),
    # ...
    path('logout/', views.logout_view, name='logout'),
    # 기타 URL 패턴들
    path('', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),  # 빈 경로(empty path)에 대한 URL 패턴 추가
]
