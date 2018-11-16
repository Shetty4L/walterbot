# walterbot

Run Rasa Core:
```bash
python -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
```

Run Action Server:
```bash
python -m rasa_core_sdk.endpoint --actions actions
```

Run Interactive:
```bash
python -m rasa_core.train --online -o models/dialogue -d domain.yml -s stories.md --endpoints endpoints.yml
```

Train Rasa Core:
```bash
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue
```

Train Rasa NLU:
```bash
python -m rasa_nlu.train -c nlu_config.yml --data nlu_data/interrogation.md -o models --fixed_model_name nlu --project current --verbose
```

Run NLU Server:
```bash
python -m rasa_nlu.server --path models/
```

Query NLU Server:
```bash
curl -XPOST localhost:5000/parse -d '{"q":"i will take 2 years off your sentence", "project": "current", "model": "nlu"}'
```
