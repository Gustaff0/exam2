"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views.poll import PollList, PollEdit, PollView, PollDelete, PollCreate
from webapp.views.choice import ChoiceCreate, ChoiceEdit, ChoiceDelete
from webapp.views.answer import CreateAnswer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollList.as_view(), name='home' ),
    path('poll/<int:pk>/edit', PollEdit.as_view(), name='edit'),
    path('poll/<int:pk>/delete', PollDelete.as_view(), name='delete'),
    path('poll/<int:pk>/view', PollView.as_view(), name='view'),
    path('poll/create', PollCreate.as_view(), name='create'),
    path('choice/create/<int:pk>', ChoiceCreate.as_view(), name='create_choice'),
    path('choice/delete/<int:pk>', ChoiceDelete.as_view(), name='delete_choice'),
    path('choice/edit/<int:pk>', ChoiceEdit.as_view(), name='edit_choice'),
    path('answer/add/<int:pk>', CreateAnswer.as_view(), name='create_answer')
]
