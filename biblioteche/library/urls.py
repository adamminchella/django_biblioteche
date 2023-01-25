from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="library-home"),
    path("books/<int:id>/", views.show, name="library-book")
]

handler404 = 'library.views.not_found_404'
