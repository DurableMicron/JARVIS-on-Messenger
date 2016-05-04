
import requests
import json
from templates.text import TextTemplate


#doesnt work as I need to fix the apikey

def process(input,entities):

    output = {}
    post_url = 'https://www.googleapis.com/urlshortener/v1/url'#api
    payload = {'longUrl': entities['shorten'][0]}#currently just guessing how the witai works until i have a better look into it
    headers = {'content-type': 'application/json'}
    try:
        r = requests.post(post_url, data=json.dumps(payload), headers=headers)
        data = r.json()
        print data
        output['input'] = input
        output['output'] = TextTemplate(data['id'])#also just a guess until i can get a good response
        output['success'] = True
    except:
        output['success'] = False
    return output

