from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionUpdateConfessLevel(Action):
	def name(self):
		# type: () -> Text
		return "action_update_confess_level"

	def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> Slots

		sentiment = float(tracker.get_slot('sentiment')) 
		fear = float(tracker.get_slot('fear')) 
		anger = float(tracker.get_slot('anger')) 
		guilt = float(tracker.get_slot('guilt')) 
		trust = float(tracker.get_slot('trust'))
		offer = int(tracker.get_slot('offer'))

		current_compliance = float(tracker.get_slot('compliance'))
		print current_compliance

		new_compliance = self.calculateCompliance(current_compliance, sentiment, fear, anger, guilt, trust, offer)
		print new_compliance
		compliance_slot = SlotSet("compliance", new_compliance)

		confess_level = None

		if new_compliance >= 0.8:
			confess_level = "high"
		elif new_compliance >= 0.5:
			confess_level = "medium"
		else:
			confess_level = "low"

		confess_level_slot = SlotSet("confess_level", confess_level)

		if confess_level == "high":
			dispatcher.utter_template("utter_confess", tracker)

		return [compliance_slot, confess_level_slot]

		# if offer >= 10:
		# 	return [SlotSet("compliance", 0.8)]
		# elif offer >= 5:
		# 	return [SlotSet("compliance", current_compliance + 0.3)]
		# elif offer >= 2:
		# 	return [SlotSet("compliance", current_compliance + 0.1)]
		# else:
		# 	return [SlotSet("compliance", 0.0)]

	def calculateCompliance(self, current_compliance, sentiment, fear, anger, guilt, trust, offer):
		return current_compliance + 0.2

class ActionConfess(Action):
	def name(self):
		# type: () -> Text
		return "action_confess"

	def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot

		return [SlotSet("confessed", True)]

class ActionIncreaseSentiment(Action):
	def name(self):
		# type: () -> Text
		return "action_increase_sentiment"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		sentiment = float(tracker.get_slot('sentiment'))
		return [SlotSet("sentiment", sentiment + 0.1)]

class ActionDecreaseSentiment(Action):
	def name(self):
		# type: () -> Text
		return "action_decrease_sentiment"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		sentiment = float(tracker.get_slot('sentiment'))
		return [SlotSet("sentiment", sentiment - 0.1)]

class ActionIncreaseFear(Action):
	def name(self):
		# type: () -> Text
		return "action_increase_fear"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		fear = float(tracker.get_slot('fear'))
		return [SlotSet("fear", fear + 0.1)]

class ActionDecreaseFear(Action):
	def name(self):
		# type: () -> Text
		return "action_decrease_fear"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		fear = float(tracker.get_slot('fear'))
		return [SlotSet("fear", fear - 0.1)]

class ActionIncreaseAnger(Action):
	def name(self):
		# type: () -> Text
		return "action_increase_anger"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		anger = float(tracker.get_slot('anger'))
		return [SlotSet("anger", anger + 0.1)]

class ActionDecreaseAnger(Action):
	def name(self):
		# type: () -> Text
		return "action_decrease_anger"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		anger = float(tracker.get_slot('anger'))
		return [SlotSet("anger", anger - 0.1)]

class ActionIncreaseGuilt(Action):
	def name(self):
		# type: () -> Text
		return "action_increase_guilt"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		guilt = float(tracker.get_slot('guilt'))
		return [SlotSet("guilt", guilt + 0.1)]

class ActionDecreaseGuilt(Action):
	def name(self):
		# type: () -> Text
		return "action_decrease_guilt"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		guilt = float(tracker.get_slot('guilt'))
		return [SlotSet("guilt", guilt - 0.1)]

class ActionIncreaseTrust(Action):
	def name(self):
		# type: () -> Text
		return "action_increase_trust"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		trust = float(tracker.get_slot('trust'))
		return [SlotSet("trust", trust + 0.1)]

class ActionDecreaseTrust(Action):
	def name(self):
		# type: () -> Text
		return "action_decrease_trust"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
		trust = float(tracker.get_slot('trust'))
		return [SlotSet("trust", trust - 0.1)]


