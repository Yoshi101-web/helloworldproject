from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloWorldView

#classの場合は、as_viewメゾッドを使う。
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloworldapp.urls'))
]

