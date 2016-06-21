from django.http import JsonResponse
from num2words import num2words


def index(request):
    liczba = request.POST.get('liczba', 0)
    return JsonResponse({
        liczba:
        num2words(
                liczba,
                lang='en',
        )
    })
