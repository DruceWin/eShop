from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin, FormView
from django.http import HttpResponseRedirect

from .forms import UrlForm
from .models import ModelShortURL
from eShopBase.settings import ALLOWED_HOSTS


class MakeShortURL(TemplateView, FormView):
    template_name = 'make_short_url.html'
    form_class = UrlForm
    success_url = reverse_lazy('shortURL:make_short_url')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['short_urls'] = ModelShortURL.objects.filter(user=self.user_id)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.user_id
        self.object.save()
        return super().form_valid(form)


def short_url(request, short_URL):
    url = ALLOWED_HOSTS[0]
    sl = f"{url}:8000/{short_URL}"
    target = get_object_or_404(ModelShortURL, short_URL=sl)
    return HttpResponseRedirect(target.long_URL)
