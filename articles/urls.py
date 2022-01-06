from django.urls import path

from .views import (
  ArticleListView,
  ArticleDetailView,
  ArticleUpdateView,
  ArticleDeleteView,
  ArticleCreateView,
)

#app_name = 'articles'

urlpatterns = [ 
        path('<int:pk>/edit/',ArticleUpdateView.as_view(),name ="edit") ,      
        path('<int:pk>/delete/',ArticleDeleteView.as_view(),name ="delete") , 
        path('<int:pk>/',ArticleDetailView.as_view(),name ="detail") ,
        path('new/',ArticleCreateView.as_view(),name ="create") ,     
        path('',ArticleListView.as_view(),name ="list") ,      
            
        ] 