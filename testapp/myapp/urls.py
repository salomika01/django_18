from django.urls import path

from myapp.views import UserRegistrationView, UserLoginView, UserLogoutView, PostListCreateView, \
    PostRetrieveUpdateDestroyView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/logout/', UserLogoutView.as_view(), name='logout'),
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
]
