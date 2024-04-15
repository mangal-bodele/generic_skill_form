from django.urls import path
from .views import *

urlpatterns = [
    path('create/', Skill_Create.as_view(),name="create_url"),
    path('list/', Skill_List.as_view(),name="list_url"),
    path('detail/<int:pk>/', Skill_Detail.as_view(),name="detail_url"),
    path('update/<int:pk>/', Skill_Update.as_view(),name="update_url"),
    path('delete/<int:pk>/', Skill_Delete.as_view(),name="delete_url")
]