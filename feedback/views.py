from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(["GET"])
def hello_world(request):
    """Hello world"""
    return JsonResponse({"message": "Hello World!"}, status=200)


class ProtectedTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                "success": True,
                "message": f"Hello {request.user.email}, you are authenticated!",
            }
        )
