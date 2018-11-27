from flask import Flask, request
from flask_cors import CORS
import sys, os
sys.path.append(os.path.abspath('../ASR'))
import SpeechToText

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import json
import threading

app = Flask(__name__)
CORS(app)
action_endpoint = EndpointConfig('http://localhost:5055/webhook')
interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

personality_attrs_file = 'personality_attr.json'

json_obj = dict()
json_obj['sentiment'] = 0.0
json_obj['fear'] = 0.0
json_obj['anger'] = 0.0
json_obj['guilt'] = 0.0
json_obj['trust'] = 0.0
json_obj['offer'] = 0
json_obj['confessed'] = False
json_obj['confess_level'] = "low"
json_obj['compliance'] = 0.0

with open(personality_attrs_file, 'w') as outfile:
    json.dump(json_obj, outfile)

t = threading.Thread()
t.start()

response_map = json.load(open('response_mapping.json', 'r'))

@app.route("/", methods=["GET"])
def getTextFromAudioFile():

    filename = request.args.get('filename')
    text = SpeechToText.convertAudioToText(filename)

    print text

    response = agent.handle_text(text)
    t.join()

    print response

    with open(personality_attrs_file, 'r') as json_file:
        json_obj = json.load(json_file)

        if len(response) > 0:
            json_obj['response'] = response[0]['text']
            json_obj["responseId"] = response_map[response[0]['text']]

        return json.dumps(json_obj)

    return json.dumps({'error': "No mapping found"})


#
# from rasa_core.agent import Agent
# from rasa_core.interpreter import RasaNLUInterpreter
# from rasa_core.utils import EndpointConfig
# import json
# import os
# import threading
#
# if __name__ == '__main__':
#     action_endpoint = EndpointConfig('http://localhost:5055/webhook')
#     interpreter = RasaNLUInterpreter('models/current/nlu')
#     agent = Agent.load('models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
#
#     t = threading.Thread()
#     t.start()
#
#     response_map = json.load(open('response_mapping.json', 'r'))
#
#     print "Enter messages:"
#     while True:
#         message = raw_input()
#         response = agent.handle_text(unicode(message, 'utf-8'))
#         t.join()
#
#         print response[0]['text'],response_map[response[0]['text']]
#
#         personality_attrs_file = 'personality_attr.json'
#         if os.path.exists(personality_attrs_file):
#             with open(personality_attrs_file, 'r') as json_file:
#                 json_obj = json.load(json_file)
#                 print json_obj
#
#         print "\n"
