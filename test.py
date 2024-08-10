from transformers import pipeline

# Load a pre-trained text generation pipeline
generator = pipeline('text-generation')

# Generate text
result = generator("Once upon a time,")
print(result)