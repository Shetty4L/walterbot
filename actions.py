from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCalculateCompliance(Action):
	def name(self):
		# type: () -> Text
		return "action_calculate_compliance"

	def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot

		# respect = tracker.get_slot('respect')
		# bonding = tracker.get_slot('bonding')
		# fear = tracker.get_slot('fear')
		# trust = tracker.get_slot('trust')
		offer = int(tracker.get_slot('offer'))
		print offer
		current_compliance = tracker.get_slot('compliance')
		print current_compliance

		if offer >= 10:
			return [SlotSet("compliance", 0.8)]
		elif offer >= 5:
			return [SlotSet("compliance", current_compliance + 0.3)]
		elif offer >= 2:
			return [SlotSet("compliance", current_compliance + 0.1)]
		else:
			return [SlotSet("compliance", 0.0)]

class ActionUpdateConfessLevel(Action):
	def name(self):
		# type: () -> Text
		return "action_update_confess_level"

	def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot

		compliance = float(tracker.get_slot('compliance'))
		print compliance

		if compliance >= 0.8:
			return [SlotSet("confess_level", "high")]
		elif compliance >= 0.5:
			return [SlotSet("confess_level", "medium")]
		else:
			return [SlotSet("confess_level", "low")]
