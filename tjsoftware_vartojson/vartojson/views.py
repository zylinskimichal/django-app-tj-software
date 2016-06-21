from django.http import JsonResponse
from num2words import num2words


def index(request):
    return JsonResponse({
        request.POST.get('liczba', 0):
        num2words(
                request.POST.get('liczba', 0),
                lang='en',
        )
    })
