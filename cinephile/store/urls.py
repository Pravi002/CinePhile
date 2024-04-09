from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name="home"),
    path('register/',views.RegView.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('movie/<int:pk>/',views.MovieView.as_view(),name="movie"),
    # path('itemdetail/<int:pk>/',views.ItemDetailView.as_view(),name="item_detail"),
 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
