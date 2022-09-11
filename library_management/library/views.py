from dataclasses import fields
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from library.models import Books
from django.http import HttpResponse
# Create your views here.

# Login page


class UserLoginView(LoginView):
    template_name = 'library/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('books')


# Registration Page {Creating a new user}

class RegistrationPage(FormView):
    template_name = 'library/user_registration.html'
    success_url = reverse_lazy('books')

    # Validation function for a book entry

    def form_valid(self, form):
        user = form.save()
        if (user is not None):
            login(self.request, user)
        return super().form_valid(form)

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('books')
        else:
            return super(RegistrationPage, self)

# CRUD OPERATIONS FOR LIBRARY


class BookList(ListView):
    model = Books
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['books']
        context['count'] = context['books'].filter(
            finish=False).count()
        return context


class BookDetail(DetailView):
    model = Books
    context_object_name = 'book'
    template_name = 'library/book.html'

# Create an entry for Books.


class BookCreate(CreateView):
    model = Books
    fields = ['title', 'author', 'finish', 'review']
    success_url = reverse_lazy('books')
    template_name = 'library/book_form.html'

# Update a book in the database


class BookUpdate(UpdateView):
    model = Books
    fields = ['title', 'author', 'finish', 'review']
    success_url = reverse_lazy('books')
    template_name = 'library/book_form.html'

# Delete a book from the database


class BookDelete(DeleteView):
    model = Books
    context_object_name = 'book'
    success_url = reverse_lazy('books')
    template_name = 'library/book_confirm_delete.html'
