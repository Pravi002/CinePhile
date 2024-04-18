from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('register/',views.RegView.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('moviedetail/<int:pk>/',views.MovieDetailView.as_view(),name="movie_detail"),
    path('watchlist/<int:pk>/',views.WatchListView.as_view(),name="watchlist"),
    path('watchlistdetail/',views.WatchListDetail.as_view(),name="watchlist_detail"),
    path('deletewatchlist/<int:pk>/',views.WatchListDelete.as_view(),name="delete_watchlist"),
    path('diary/<int:pk>/',views.DiaryView.as_view(),name="diary"),
    path('diarydetail/',views.DiaryDetail.as_view(),name="diary_detail"),
    path('deletediary/<int:pk>/',views.DiaryDelete.as_view(),name="delete_diary"),
    path('myprofile/',views.ProfileView.as_view(),name="myprofile"),
    path('genre/<str:genre>/',views.MovieGenre.as_view(),name="genre"),
    path('language/<str:language>/',views.MovieLanguage.as_view(),name="language"),

 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
