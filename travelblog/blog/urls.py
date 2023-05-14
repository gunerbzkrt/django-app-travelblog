from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.post_list, name="post_list"), 
    path("post/<int:pk>", views.post_detail, name="post_detail"), 
    path("region/<slug:slug>",views.post_by_region, name="post_by_region"),
    path("post/new", views.post_new, name="post_new"), 
    path("post/edit/<int:pk>", views.post_edit, name="post_edit"),
    path('search/', views.search, name='search'),
    path('comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
