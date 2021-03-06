from django.urls import path
from . import views

urlpatterns = [
    path('', views.menulist, name='blog-home'),
    path('menu/<city>/<zone>', views.menubyzone, name='menubyzone'),
    path('post/autocomplete/', views.autocomplete, name='autocomplete'),
    path('post/set_city/<cityname>', views.set_city, name='set_city'),
    path('post/pin/<username>', views.pin, name='pin'),
    path('post/unpin/<username>', views.unpin, name='unpin'),
    path('post/<int:pk>/update', views.update_menu, name='post-update'),
    path('post/<int:pk>/delete', views.delete_menu, name='post-delete'),
    path('post/<int:pk>/activate', views.activate, name='activate'),
]