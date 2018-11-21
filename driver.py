from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import json
import os
import threading

if __name__ == '__main__':
    action_endpoint = EndpointConfig('http://localhost:5055/webhook')
    interpreter = RasaNLUInterpreter('models/current/nlu')
    agent = Agent.load('models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

    t = threading.Thread()
    t.start()

    print "Enter messages:"
    while True:
        message = raw_input()
        if message == 'stop':
            break
        response = agent.handle_message(unicode(message, "utf-8"))
        t.join()
        print response

        personality_attrs_file = 'personality_attr.json'
        if os.path.exists(personality_attrs_file):
            with open(personality_attrs_file, 'r') as json_file:
                json_obj = json.load(json_file)
                print json_obj
