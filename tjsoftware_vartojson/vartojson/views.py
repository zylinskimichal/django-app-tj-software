from django.http import JsonResponse


def index(request):
    return JsonResponse({'liczba': request.POST.get('bar', 0)})
