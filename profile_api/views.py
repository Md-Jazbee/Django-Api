from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, formate=None):
        '''Return a list of APIView features'''
        an_apiview = [
            'User HTTP metheds as function ( get , post , put , patch , delete)',
            'Is similar to a traditional over you application logic',
            'hello world',
            ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

