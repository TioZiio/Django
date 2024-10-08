from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.singleContact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    
    # user 
    path('user/create/', views.register, name='user_register'),
    path('user/login/', views.login_view, name='user_login'),
    path('user/logout/', views.logout_view, name='user_logout'),
    path('user/update/', views.update_view, name='user_update'),
]
