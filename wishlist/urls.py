from django.urls import path
from wishlist.views import show_wishlist, show_xml, \
    show_xml_by_id, register, login_user, logout_user, wishlist_ajax, create_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', wishlist_ajax, name='wishlist_ajax'),
    path('ajax/submit', create_wishlist, name='create_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]