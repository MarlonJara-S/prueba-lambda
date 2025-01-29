from django.urls import path
from .views import (
    RegisterView, LoginView, UserListView, UserEditView, UserDesactivateView, TokenRefreshView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>/', UserEditView.as_view(), name='user-edit'),
    path('users/<int:pk>/deactivate/', UserDesactivateView.as_view(), name='user-deactivate'),
]   