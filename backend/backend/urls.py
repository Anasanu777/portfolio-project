from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from feedback.views import FeedbackViewSet

router = routers.DefaultRouter()
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
