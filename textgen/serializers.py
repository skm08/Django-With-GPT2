from rest_framework import serializers

class TextGenSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=200)
    generated_text = serializers.CharField(max_length=500, read_only=True)