from django.urls import path

from . import views


app_name = 'food'
urlpatterns = [
    path('type/list/', views.TypeListGenericView.as_view(), name='type-list'),
    path('type/<int:pk>/detail/', views.TypeDetailGenericView.as_view(), name='type-detail'),

    path('food/list/', views.FoodListGenericView.as_view(), name='food-list'),
    path('food/<int:pk>/detail/', views.FoodDetailGenericView.as_view(), name='food-detail'),

    path('comment/list/', views.CommentListMixinView.as_view(), name='comment-list'),
    path('comment/<int:pk>/detail/', views.CommentDetailMixinView.as_view(), name='comment-detail'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]