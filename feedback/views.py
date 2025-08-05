from django.http import JsonResponse


def hello_world(request):
    """Hello world"""
    return JsonResponse({"message": "Hello World!"}, status=200)
