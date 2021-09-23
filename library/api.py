from rest_framework import routers
from api import views

#Asosoiy proyektimiz ichida yozilgan
#Bu yerda viewlarni ruyhatdan utkazib olamiz
router = routers.DefaultRouter()
router.register(r'books',views.BookViewSet,basename='book')
router.register(r'lib-users',views.LibuserViewSet)
router.register(r'rented-books',views.RentBookViewSet)
#router.register('ln/languages', views.LanguageView, basename='languages')