from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('', views.lista_postow, name='lista_postow'),
    path("search/", views.post_search, name="post_search"),
    path('tag/<slug:tag_slug>/',views.lista_postow,name="lista_postow_po_tagach"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share',views.post_share,name='post_share')
]

