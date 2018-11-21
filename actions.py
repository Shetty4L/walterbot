from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import json

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
        offer_type = tracker.get_slot('offer_type')

        current_compliance = float(tracker.get_slot('compliance'))
        print current_compliance

        new_compliance = self.calculateCompliance(current_compliance, sentiment, fear, anger, guilt, trust, offer)
        print new_compliance
        compliance_slot = SlotSet("compliance", new_compliance)

        confess_level = None

        if new_compliance >= 0.75:
            confess_level = "high"
        elif new_compliance >= 0.5:
            confess_level = "medium"
        else:
            confess_level = "low"

        confess_level_slot = SlotSet("confess_level", confess_level)

        has_confessed = tracker.get_slot('confessed')

        print "Sentiment: {sentiment}\nFear: {fear}\nAnger: {anger}\nGuilt: {guilt}\nTrust: {trust}\nOffer: {offer}\nConfessed: {confessed}\n".format(sentiment=sentiment, fear=fear, anger=anger, guilt=guilt, trust=trust, offer=offer, confessed=has_confessed)

        json_obj = dict()
        json_obj['sentiment'] = sentiment
        json_obj['fear'] = fear
        json_obj['anger'] = anger
        json_obj['guilt'] = guilt
        json_obj['trust'] = trust
        json_obj['offer'] = offer
        json_obj['confessed'] = has_confessed
        json_obj['confess_level'] = confess_level
        json_obj['compliance'] = new_compliance

        with open('personality_attr.json', 'w') as outfile:
            json.dump(json_obj, outfile)

        if (not has_confessed) and (confess_level == "high" or confess_level == "medium"):
            confessed_slot = SlotSet("confessed", True)
            dispatcher.utter_template("utter_confess", tracker)
            return [compliance_slot, confess_level_slot, confessed_slot]
        # elif not has_confessed and offer_type != "bad":
            # dispatcher.utter_template("utter_deny", tracker)

        return [compliance_slot, confess_level_slot]

    def calculateCompliance(self, current_compliance, sentiment, fear, anger, guilt, trust, offer):
        # sentiment: [-1, 1]
        # fear: [0, 1]
        # anger: [0, 1]
        # guilt: [0, 1]
        # trust: [0, 1]
        # offer: [0, 20]
        normalized_sentiment = self.__normalize(sentiment, (-1, 1))
        normalized_fear = self.__normalize(fear, (0, 1))
        normalized_anger = self.__normalize(anger, (0, 1))
        normalized_guilt = self.__normalize(guilt, (0, 1))
        normalized_trust = self.__normalize(guilt, (0, 1))
        normalized_offer = self.__normalize(offer, (0, 20))

        # Minimization
        compliance_min = 0.60*normalized_trust + 0.4*normalized_sentiment + 0.2*normalized_guilt - 0.2*normalized_anger

        # Maximization
        compliance_max = 0.75*normalized_fear + 0.5*normalized_guilt - 0.25*normalized_anger

        # Promise
        compliance_promise = 0.40*normalized_offer + 0.40*normalized_trust + 0.2*normalized_sentiment

        # Threat
        compliance_threat = 1.2*normalized_fear - 0.2*normalized_anger

        new_compliance = max([compliance_min, compliance_max, compliance_promise, compliance_threat])

        return new_compliance

    def __normalize(self, value, range):
        return (1.0 * (value - range[0]) / (range[1] - range[0]))

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
        return [SlotSet("sentiment", sentiment + 0.2)]

class ActionDecreaseSentiment(Action):
    def name(self):
    # type: () -> Text
        return "action_decrease_sentiment"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        sentiment = float(tracker.get_slot('sentiment'))
        return [SlotSet("sentiment", sentiment - 0.2)]

class ActionIncreaseFear(Action):
    def name(self):
    # type: () -> Text
        return "action_increase_fear"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        fear = float(tracker.get_slot('fear'))
        return [SlotSet("fear", fear + 0.2)]

class ActionDecreaseFear(Action):
    def name(self):
    # type: () -> Text
        return "action_decrease_fear"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        fear = float(tracker.get_slot('fear'))
        return [SlotSet("fear", fear - 0.2)]

class ActionIncreaseAnger(Action):
    def name(self):
    # type: () -> Text
        return "action_increase_anger"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        anger = float(tracker.get_slot('anger'))
        return [SlotSet("anger", anger + 0.2)]

class ActionDecreaseAnger(Action):
    def name(self):
    # type: () -> Text
        return "action_decrease_anger"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        anger = float(tracker.get_slot('anger'))
        return [SlotSet("anger", anger - 0.2)]

class ActionIncreaseGuilt(Action):
    def name(self):
    # type: () -> Text
        return "action_increase_guilt"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        guilt = float(tracker.get_slot('guilt'))
        return [SlotSet("guilt", guilt + 0.2)]

class ActionDecreaseGuilt(Action):
    def name(self):
    # type: () -> Text
        return "action_decrease_guilt"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        guilt = float(tracker.get_slot('guilt'))
        return [SlotSet("guilt", guilt - 0.2)]

class ActionIncreaseTrust(Action):
    def name(self):
    # type: () -> Text
        return "action_increase_trust"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        trust = float(tracker.get_slot('trust'))
        return [SlotSet("trust", trust + 0.2)]

class ActionDecreaseTrust(Action):
    def name(self):
    # type: () -> Text
        return "action_decrease_trust"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        trust = float(tracker.get_slot('trust'))
        return [SlotSet("trust", trust - 0.2)]

class ActionAssessOffer(Action):
    def name(self):
    # type: () -> Text
        return "action_assess_offer"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot
        offer = int(tracker.get_slot('offer'))

        if offer < 7:
            return [SlotSet("offer_type", "bad")]

        return [SlotSet("offer_type", "good")]

class ActionResetOfferFlag(Action):
    def name(self):
    # type: () -> Text
        return "action_reset_offer_flag"

    def run(self, dispatcher, tracker, domain):
    # type: (Dispatcher, DialogueStateTracker, Domain) -> Slot

        return [SlotSet("offer_type", "no_offer")]
