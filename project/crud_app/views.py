from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Skill


class Skill_Create(CreateView):
    model = Skill
    fields = "__all__"
    success_url = reverse_lazy("list_url")


class Skill_List(ListView):
    model = Skill


class Skill_Detail(DetailView):
    model = Skill


class Skill_Update(UpdateView):
    model = Skill
    fields = "__all__"
    success_url = reverse_lazy("list_url")



class Skill_Delete(DeleteView):
    model = Skill
    success_url = reverse_lazy("list_url")

