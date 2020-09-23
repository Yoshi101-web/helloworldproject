from django.urls import path
from .views import hellofunction

#classの場合は、as_viewメゾッドを使う。
urlpatterns = [
    path('world/', hellofunction),
]

