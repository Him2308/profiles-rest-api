from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView Features."""

        an_apiview = [
            'Uses HTTP methods As function(get ,post,patch,put,delete)',
            'It is similar to a tradditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLs'

        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
        
