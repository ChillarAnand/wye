from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from braces import views

from .forms import OrganisationForm
from .models import Organisation


class OrganisationCreate(views.LoginRequiredMixin, generic.CreateView):
    model = Organisation
    form_class = OrganisationForm
    template_name = 'organisation/create.html'
    success_url = reverse_lazy('home-page')

    def get_queryset(self):
        return Organisation.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        form = OrganisationForm(data=request.POST)
        if form.is_valid():
            form.instance.save()
            form.instance.user.add(request.user)
            form.instance.save()
            # send email on new organisation created
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


class OrganisationDetail(views.LoginRequiredMixin, generic.DetailView):
    model = Organisation
    template_name = 'organisation/detail.html'
    success_url = reverse_lazy('home-page')

    def get_queryset(self):
        return Organisation.objects.filter(user=self.request.user)


class OrganisationUpdate(views.LoginRequiredMixin, generic.UpdateView):
    model = Organisation
    form_class = OrganisationForm
    template_name = 'organisation/edit.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return Organisation.objects.get(user=self.request.user, id=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        self.object = self.object()
        form = OrganisationForm(data=request.POST)
        if form.is_valid():
            if kwargs['action'] == 'edit':
                self.object.save()
            # Need to test this part of code
            if kwargs['action'] == 'deactive':
                self.object.active = False
                self.object.save()
                # send email on new organisation created
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
