# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    vice_text = request.GET['vicetext']
    reversed_text = vice_text[::-1]
    word_count = len(vice_text.split())
    # print(vice_text)
    return render(request, 'reverse.html', {'vicetext': vice_text,
                                            'reversedtext': reversed_text,
                                            'wordcount': word_count})
