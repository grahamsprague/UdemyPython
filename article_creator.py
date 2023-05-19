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
    'Write me a short story in the first person about a trip to the store for Korbin and his friend Ignacio. Both are heavily self-medicating with LSD and mescaline. Make the style of the story gonzo like Fear and Loathing in Las Vagas. Have the duo go offtrack on some zaney adventures but end up back home. Have the story end with Ignacio waking up in a tree in the wee hours of the AM.',

    
]

counter = 0

for idea in ideas:

    counter += 1

    prompt = '''
    Reply only in json. You are a writer for a website and you write articles in perfectly valid JSON. Write an article with 10 paragraphs about [TOPIC] Use [FORMAT] using [VOICE].
    [TOPIC]: ''' + idea + '''
    [VOICE]: Satire, Zaney
    [FORMAT]: JSON, using the following format,
    {"paragraphs":["string"]}
    '''



    

    # print(prompt)

    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1500, temperature=0.7)
    my_paragraphs = response.choices[0].text


    prompt2 = '''
    Reply only in json.  Generate between 8 and 12 comments for the follwing article(some just a few worss and some several sentences), with creative usernames(no spaces). Make the comments a mix or for and against the article:[ARTICLE]. Use this format: [FORMAT]
    [FORMAT]: "comments":[]
    [ARTICLE]: ''' + my_paragraphs



    response = openai.Completion.create(engine=model_engine, prompt=prompt2, max_tokens=1500, temperature=0.7)
    my_comments = response.choices[0].text

    my_json = '[{"article": {"short_name":"string","article_id": 0,"author_id": 38,"category_id": 0,"publish_date" : "2023-XX-XX","titles":["string"],'+ my_paragraphs +','+ my_comments +'}]'

 


    f = open(str(filename)+ '_' + str(counter) + '.json', "w")
    f.write(my_json)
    f.close()

    print(my_json)

print('done processing')