from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''
    Serializar un campo
    '''

    name = serializers.CharField(max_length = 20)