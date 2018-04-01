from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""

        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'It is similar to a traditional django view',
            'Gives you the most control over the logic',
            'Is mapped manully to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
