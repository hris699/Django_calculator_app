from rest_framework import serializers

class MemorySerializer(serializers.Serializer):
    number=serializers.CharField(max_length=50)

