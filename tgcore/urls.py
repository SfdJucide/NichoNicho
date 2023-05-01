from django.urls import path
from tgcore.views import catalog, feedback, succsess_message

app_name = 'tgcore'

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('feedback/', feedback, name='feedback'),
    path('succsess_message/', succsess_message, name='succsess_message'),
]