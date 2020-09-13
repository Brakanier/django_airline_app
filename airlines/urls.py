from django.urls import path

from airlines.views import AirlineView

urlpatterns = [
    path('airlines/', AirlineView.as_view()),
    path('airlines/<int:pk>', AirlineView.as_view()),
]