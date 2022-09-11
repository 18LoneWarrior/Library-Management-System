from django.urls import path
from .views import RegistrationPage, BookCreate, BookDetail, BookList, BookUpdate, BookDelete, UserLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', BookList.as_view(), name="books"),
    path('login/', RegistrationPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegistrationPage.as_view(), name='register'),
    path('book/<int:pk>', BookDetail.as_view(), name="book"),
    path('create_book/', BookCreate.as_view(), name="create_book"),
    path('update_book/<int:pk>', BookUpdate.as_view(), name="update_book"),
    path('delete_book/<int:pk>', BookDelete.as_view(), name="delete_book"),
]
