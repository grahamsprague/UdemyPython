import os
from datetime import datetime
from dotenv import load_dotenv
import openai

load_dotenv()

now = datetime.now()

filename = now.strftime("%Y-%m-%d-%H_%M_%S")

print('filename:'+filename)

openai.api_key = os.getenv('OPENAI_API_KEY')
model_engine = "text-davinci-003"


ideas = [
    'Conglomaco infinite cat theorem experiment. If we give lots of cats, lots of time with a musical keyboard, eventually they will prodouce Beethovens 5th.',

    
]

counter = 0

for idea in ideas:

    counter += 1

    prompt = '''
    Reply only in json. You are a writer for a website and you write articles in perfectly valid JSON. Write an article about [TOPIC] Use [FORMAT] using [VOICE]. Create a list of titles and a short_name. Generate some comments(some just a few worss and some several sentences), with creative usernames(no spaces). Make the comments a mix or for and against the article topic.
    [TOPIC]: ''' + idea +'''
    [VOICE]: Satire
    [FORMAT]: JSON, using the following format,
    [{"article": {"short_name":"string","titles":["string"],"paragraphs":["string"]},"comments":[]}]
    '''

    # print(prompt)

    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1500, temperature=0.7)
    text = response.choices[0].text

    f = open(str(filename)+ '_' + str(counter) + '.json', "w")
    f.write(text)
    f.close()

    print(text)

print('done processing')