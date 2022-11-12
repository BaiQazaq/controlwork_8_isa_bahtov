from django.urls import path

from accounts.views.login_view import LoginView
from accounts.views.logout_view import logout_view
from accounts.views.register_view import RegisterView
# from accounts.views.acc_profile_view import ProfileView
# from accounts.views.acc_change_view import UserChangeView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

#     path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
#     path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),