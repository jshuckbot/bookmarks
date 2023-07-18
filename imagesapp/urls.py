from django.urls import path

from imagesapp import views

app_name = "imagesapp"

urlpatterns = [path("create/", views.image_create, name="create")]
