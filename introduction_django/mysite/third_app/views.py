from django.shortcuts import render
import random

# Create your views here.


def index(request):
    def title():
        color_list = ['yellow', 'black', 'white', 'green', 'orange', 'purple']
        for item in color_list:
            return item

    def logo():
        pass

    def menu():
        pass

    def content():
        pass

    def key_information():
        pass

    def footer():
        pass

    template = 'third_app/index.html'
    context = {
        'title': title(),
        # 'logo': logo(),
        # 'menu': menu(),
        # 'content': content(),
        # 'key_information': key_information(),
        # 'footer': footer,
    }
    return render(request, template, context)

