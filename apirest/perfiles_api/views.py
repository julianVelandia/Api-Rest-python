from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from perfiles_api import serializer


class HelloApiview(APIView):
    serializer_class = serializer.HelloSerializer


    
    def get(self, request, format=None):
        '''
        Retorna la lista con las características del usuario
        '''

        an_apiview = [
            'Metodos http: get, post, patch, put y delete',
            'item 2',
            'item 3',
            'item 4',
        ]
        
        return Response({'mensaje': 'Hello', 'an_apiview': an_apiview})


    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            mensaje = f'Hola {name}'
            return Response({'mensaje':mensaje})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):

        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        'Actualización parcial'

        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):

        return Response({'method':'DELETE'})

