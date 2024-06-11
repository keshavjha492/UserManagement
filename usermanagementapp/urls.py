from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, ProductListView, ProductDetailView, OrderCreateView, OrderHistoryView, CartView

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/user/profile/', UserProfileView.as_view()),
    path('api/products/', ProductListView.as_view()),
    path('api/products/<pk>/', ProductDetailView.as_view()),
    path('api/orders/', OrderCreateView.as_view()),
    path('api/orders/history/', OrderHistoryView.as_view()),
    path('api/cart/', CartView.as_view()),
]