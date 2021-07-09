from django.urls import path
from django.urls.conf import include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="income"),
    path('add-income', views.add_income, name="add-income"),
    path('preferences/', include('userpreferences.urls')),
    path('edit-income/<int:id>', views.income_edit, name="edit-income"),
    path('delete-income/<int:id>', views.income_delete, name="delete-income"), ]
