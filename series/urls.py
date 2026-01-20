from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Genres
    path('genres/', views.genres, name='genres'),
    path('genre/<str:genre>/', views.genre_detail, name='genre_detail'),
    

    # Series
    path('series/<int:pk>/', views.series_info, name='series-info'),
    path('series/', views.series_list, name='series_list'),

    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Profile
    path('profile/<str:username>/', views.user_profile, name='user_profile'),


    # Favorites
    path('add_favorite/<int:series_id>/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:series_id>/', views.remove_favorite, name='remove_favorite'),
]
