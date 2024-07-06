from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.RegisterUser.as_view(),name='Register'),
    path('login/',views.CustomTokenObtainPairView.as_view(),name='Login'),
    path('urladd/',views.UrlCreateview.as_view(),name='urlcreate'),
    path('userurlview/<int:id>/', views.UrlListview.as_view(), name='userurlview'),
    path('urlupadatedelet/<int:pk>/',views.Urlview.as_view(),name="urlupdatedeleteview")
]