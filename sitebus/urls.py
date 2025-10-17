from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("dashboard/<slug:slug>/", views.manage_gallery, name="manage_gallery"),
    path("contact/", views.contact_view, name="contact"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
