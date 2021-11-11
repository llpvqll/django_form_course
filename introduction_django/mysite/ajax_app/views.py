from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class MainView(TemplateView):
    template_name = 'ajax_index.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
