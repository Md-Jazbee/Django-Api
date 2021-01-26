from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializer

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializer.HelloSerializer

    def get(self, request, formate=None):
        '''Return a list of APIView features'''
        an_apiview = [
            'User HTTP metheds as function ( get , post , put , patch , delete)',
            'Is similar to a traditional over you application logic',
            'hello world',
            ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
        
    
    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
            
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,pk=None):
        '''Handle Updating an object pk is Primary key'''
        return Response({'methed':'PUT'})

    def patch(self,request,pk=None):
        '''Handle a partial update of an object'''
        return Response({'methed':'PATCH'})

    def delete(self,request,pk=None):
        '''Handle Delete an Object'''
        return Response({'methed':'DELETE'})



