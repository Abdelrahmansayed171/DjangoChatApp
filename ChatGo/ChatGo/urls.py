from django.contrib import admin
from django.urls import path, include
from ChatRoom import views,urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ChatRoom', include('ChatRoom.urls',namespace='chatroom')),
]
