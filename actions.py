from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionUpdateConfessLevel(Action):
	def name(self):
		# type: () -> Text
		return "action_update_confess_level"

	def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot

		sentiment = int(tracker.get_slot('sentiment'))
		fear = int(tracker.get_slot('fear')) 
		anger = int(tracker.get_slot('anger')) 
		guilt = int(tracker.get_slot('guilt')) 
		trust = int(tracker.get_slot('trust'))
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
		new_compliance = 0.8
		return new_compliance

class ActionConfess(Action):
	def name(self):
		# type: () -> Text
		return "action_confess"

	def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot

		return [SlotSet("confessed", True)]
