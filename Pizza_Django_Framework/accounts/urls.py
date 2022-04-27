from django.urls import path

from Pizza_Django_Framework.accounts.views import logout_user, RegisterView, ProfileDetailsView, LoginUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
)