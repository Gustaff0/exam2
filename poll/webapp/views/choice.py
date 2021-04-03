from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm, SearchForm
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode

class ChoiceEdit(UpdateView):
    model = Choice
    template_name = 'choice/edit.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.poll.pk})


class ChoiceCreate(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return super(ChoiceCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.poll.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return context


class ChoiceDelete(DeleteView):
    template_name = 'choice/delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse_lazy('view', kwargs={'pk': self.object.poll.pk})

