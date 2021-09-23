from django.urls import path
from django.urls import path,include

from api.views import BookCatelogyListView

urlpatterns = []

urlpatterns += [
    path('category-list/', BookCatelogyListView.as_view())
]