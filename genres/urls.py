from django.urls import path
from . import views

urlpatterns = [
    # path('genres/',views.genre_create_list_view,name='genre-create-list'),
    path('genres/',views.GenreCreateListView.as_view(),name='genre-create-list'),
    # path('genres/<int:pk>/',views.genre_detail_view,name='genre-detail-view'),
    path('genres/<int:pk>/',views.GenreRetrieveUpdateDestroyView.as_view(),name='genre-detail-view'),
]
