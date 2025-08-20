from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # Use EITHER the function-based or class-based view for index
    # Here I'm keeping class-based as it's more reusable
    path("", views.IndexView.as_view(), name="index"),

    # Detail page using class-based view
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # Results page using class-based view
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # Vote view is only defined as a function-based view, so keep it
    path("<int:question_id>/vote/", views.vote, name="vote"),
]


