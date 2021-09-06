from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .forms import LandRegister
from .models import LandInfo
# Create your views here.

class LandInfoListView(ListView):
    context_object_name = 'lands'
    model=LandInfo
    template_name = 'activities/land_info_list.html'


class UserLandInfoListView(ListView):
    context_object_name = 'lands'
    model=LandInfo
    template_name = 'activities/user_land_info_list.html'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        queryset = LandInfo.objects.filter(owner=user)
        return queryset

class LandInfoDetailView(DetailView):
    model=LandInfo
    context_object_name = 'land'
    template_name = 'activities/land_info_detail.html'

class UserLandInfoDetailView(DetailView):
    model=LandInfo
    context_object_name = 'land'
    template_name = 'activities/user_land_info_detail.html'

class LandInfoCreateView(CreateView):
    form_class = LandRegister
    model=LandInfo
    context_object_name = 'land'
    template_name = 'activities/land_info_create.html'


    def get_success_url(self):
        return reverse_lazy('activities:land_info_list')


    def form_valid(self, form, *args, **kwargs):
        fm = form.save(commit=False)
        fm.owner = self.request.user
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LandInfoUpdateView(UpdateView):
    form_class = LandRegister
    template_name = 'activities/land_info_update.html'
    context_object_name = 'land'
    model=LandInfo

    def get_success_url(self):
        return reverse_lazy('activities:land_info_list')

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.owner = self.request.user
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LandInfoDeleteView(DeleteView):
    model= LandInfo
    context_object_name = 'land'
    template_name = 'activities/land_info_delete.html'

    def get_success_url(self):
        return reverse_lazy('activities:land_info_list')

