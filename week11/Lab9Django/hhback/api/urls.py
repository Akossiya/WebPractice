from django.urls import path

from . import views

urlpatterns = [
    path('companies/', views.company_list),
    path('vacancies/', views.vacancy_list1),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail),
    path('companies/<int:company_id>/', views.company_detail),
    path('companies/<int:company_id>/vacancies/', views.vacancy_list2),
    path('vacancies/top_ten', views.vacancy_order),

]