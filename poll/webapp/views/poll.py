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
    paginate_by = 10
    paginate_orphans = 2

    # def get(self, request, **kwargs):
    #     self.form = SearchForm(request.GET)
    #     self.search_data = self.get_search_data()
    #     return super(PollList, self).get(request, **kwargs)
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     if self.search_data:
    #         queryset = queryset.filter(
    #             Q(question__icontains=self.search_data)
    #         )
    #     return queryset