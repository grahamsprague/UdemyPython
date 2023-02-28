import openai


openai.api_key = "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"
model_engine = "text-davinci-002"


prompt = "Can you write me a python function for finding prime numbers in a range?"
response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=100) 
text = response.choices[0].text 
print(text)