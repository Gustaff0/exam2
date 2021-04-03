from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import PollForm, ChoiceForm, SearchForm
from webapp.models import Poll, Choice
from django.db.models import Q
from django.utils.http import urlencode

class PollList(ListView):
    template_name = 'poll/list.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ('question', '-created_at')
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(PollList, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(question__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class PollCreate(CreateView):
    template_name = 'poll/create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('view', kwargs={'pk' : self.object.pk})


class PollEdit(UpdateView):
    model = Poll
    template_name = 'poll/edit.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})


class PollView(DetailView):
    model = Poll
    template_name = 'poll/view.html'


class PollDelete(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('home')