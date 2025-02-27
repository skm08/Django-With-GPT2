from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

# Initialize the text generation pipeline (loads GPT-2 by default)
generator = pipeline("text-generation", model="gpt2")

def index(request):
    return render(request, 'textgen/index.html')

@api_view(['POST'])
def generate_text(request):
    prompt = request.data.get('prompt', '')
    if not prompt:
        return Response({'error': 'No prompt provided'}, status=400)
    
    # Generate text
    result = generator(prompt, max_length=50, num_return_sequences=1)
    generated_text = result[0]['generated_text']
    
    return Response({'generated_text': generated_text})