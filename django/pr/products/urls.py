from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home),
    path('search/', views.search),
    path('create/', views.create_post),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('reset_pass/', views.reset_pass),
    path('blog/<int:pk>/', views.detail_view),
    path('comment/', views.comment),
    path('reply/', views.reply),
    path('blog/update/<int:pk>/', views.update_view),
    path('blog/delete/<int:pk>/', views.delete_view),
]
