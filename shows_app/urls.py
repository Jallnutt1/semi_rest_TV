from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/<int:show_id>',views.feature),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/delete/<int:show_id>', views.delete),

]
