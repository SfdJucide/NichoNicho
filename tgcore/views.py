from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from tgcore.models import Product, TgUser
from tgcore.forms import CustomerMessageeForm
from tgcore.management.commands.bot import send_data


def catalog(request):
    return render(request, 'tgcore/catalog.html', {'products': Product.objects.all()})

def succsess_message(request):
    return render(request, 'tgcore/succsess_message.html')


def feedback(request):
    if request.method == 'POST':
        form = CustomerMessageeForm(data=request.POST)
        if form.is_valid():
            form.save()
            send_data(f"{TgUser.objects.get(pk=request.POST.get('user')).username} - {TgUser.objects.get(pk=request.POST.get('user')).user_id}\n{request.POST.get('message')}")
            return HttpResponseRedirect(reverse('tgcore:succsess_message'))
        else:
            print(form.cleaned_data)
            print(form)
    else:
        tg_user = TgUser.objects.get(user_id=request.GET.get('user_id'))
        form = CustomerMessageeForm(initial={'user': tg_user})
        title = 'Задайте ваш вопрос' if request.GET.get('q') == '1' else 'Оставьте отзыв или предложение'
        return render(request, 'tgcore/form.html', {'form': form, 'title': title})
    