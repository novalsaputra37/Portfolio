from unicodedata import name
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('mail/', send_mail, name='send_mail'),
]