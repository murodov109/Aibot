import random

class TextGenerationAI:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_text(self, prompt, length=50):
        # Simulating text generation (placeholder)
        words = prompt.split() + ["AI-generated word" + str(i) for i in range(length)]
        random.shuffle(words)
        return ' '.join(words[:length])

# Example usage:
if __name__ == '__main__':
    ai = TextGenerationAI('GPT-3')
    print(ai.generate_text('Once upon a time'))