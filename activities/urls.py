from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('land_info_list/', views.LandInfoListView.as_view(), name='land_info_list'),
    path('user_land_info_list/', views.UserLandInfoListView.as_view(), name='user_land_info_list'),
    path('create/', views.LandInfoCreateView.as_view(), name='land_info_create'),
    path('<int:pk>/update/', views.LandInfoUpdateView.as_view(), name='land_info_update'),
    path('<int:pk>/', views.LandInfoDetailView.as_view(), name='land_info_detail'),
    path('detail/<int:pk>/', views.UserLandInfoDetailView.as_view(), name='user_land_info_detail'),
    path('<int:pk>/delete/', views.LandInfoDeleteView.as_view(), name='land_info_delete'),
]
