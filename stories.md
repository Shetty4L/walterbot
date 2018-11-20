## say hello
* greet
  - action_increase_sentiment
  - slot{"sentiment": 0.1}
  - utter_greet

## formalities
* pre_recite_miranda
    - utter_affirmative

## formalities: recite_miranda
* recite_miranda
    - utter_affirmative

## filler convo
* filler_conversation
    - utter_affirmative

## asking for confession high level
* ask_confession
  - slot{"confess_level" : "high"}
  - action_confess
  - slot{"confessed": true}

## asking for confession medium level
* ask_confession
  - slot{"confess_level" : "medium"}
  - action_confess

## asking for confession low level
* ask_confession
  - slot{"confess_level" : "low"}
  - utter_deny

## ask details


## give bad offer
* give_offer {"offer": "2"}
  - action_assess_offer
  - slot{"offer_type": "bad"}
  - action_update_confess_level
  - slot{"confess_level" : "low"}
  - utter_react_bad_offer
  - action_reset_offer_flag
  - slot{"offer_type": "no_offer"}

## give good offer and low confess level
* give_offer {"offer": "10"}
  - action_assess_offer
  - slot{"offer_type": "good"}
  - action_update_confess_level
  - slot{"confess_level" : "low"}
  - utter_react_good_offer
  - action_reset_offer_flag
  - slot{"offer_type": "no_offer"}

## give good offer and medium confess level
 * give_offer {"offer": "10"}
   - action_assess_offer
   - slot{"offer_type": "good"}
   - action_update_confess_level
   - slot{"confess_level" : "medium"}
   - action_reset_offer_flag
   - slot{"offer_type": "no_offer"}

## give good offer and high confess level
    * give_offer {"offer": "10"}
      - action_assess_offer
      - slot{"offer_type": "good"}
      - action_update_confess_level
      - slot{"confess_level" : "high"}
      - action_reset_offer_flag
      - slot{"offer_type": "no_offer"}

## say goodbye
* goodbye
  - utter_goodbye

## threatening and low confess level
* threaten_suspect
  - action_increase_fear
  - slot{"fear": 0.7}
  - action_update_confess_level
  - slot{"confess_level": "low"}
  - utter_react_threat

## threatening and medium confess level
* threaten_suspect
  - action_increase_fear
  - slot{"fear": 0.7}
  - action_update_confess_level
  - slot{"confess_level": "medium"}

## threatening and low confess level
* threaten_suspect
  - action_increase_fear
  - slot{"fear": 0.7}
  - action_update_confess_level
  - slot{"confess_level": "high"}

## threatening family
* threaten_family
  - utter_react_family_threat
  - action_increase_anger
  - action_decrease_sentiment
  - action_decrease_trust
  - action_update_confess_level

## reassuring and low confess level
* reassure
  - action_increase_trust
  - slot{"trust": 0.3}
  - action_increase_sentiment
  - action_update_confess_level
  - slot{"compliance": 0.2}
  - slot{"confess_level": "low"}
  - utter_react_reassure

## reassuring and medium confess level
* reassure
  - action_increase_trust
  - slot{"trust": 0.3}
  - action_increase_sentiment
  - action_update_confess_level
  - slot{"compliance": 0.2}
  - slot{"confess_level": "medium"}

## reassuring and medium confess level
* reassure
  - action_increase_trust
  - slot{"trust": 0.3}
  - action_increase_sentiment
  - action_update_confess_level
  - slot{"compliance": 0.2}
  - slot{"confess_level": "high"}

## judging
* judge
  - utter_react_judgement
  - action_increase_anger
  - slot{"anger": 0.1}
  - action_decrease_sentiment
  - action_update_confess_level

## make guilty and low confess level
* evoke_guilt
  - utter_react_evoke_guilt
  - action_increase_guilt
  - slot{"guilt": 0.6}
  - action_update_confess_level

## make guilty and medium confess level
* evoke_guilt
  - action_increase_guilt
  - slot{"guilt": 0.6}
  - action_update_confess_level

## make guilty and medium confess level
* evoke_guilt
  - action_increase_guilt
  - slot{"guilt": 0.6}
  - action_update_confess_level

## empathising and low confess level
* empathise
  - utter_react_empathise
  - action_increase_sentiment
  - slot{"sentiment": 0.6}
  - action_increase_trust
  - action_update_confess_level
  - slot{"compliance": 0.8}
  - slot{"confess_level": "low"}

## empathising and medium confess level
* empathise
  - action_increase_sentiment
  - slot{"sentiment": 0.6}
  - action_increase_trust
  - action_update_confess_level
  - slot{"compliance": 0.8}
  - slot{"confess_level": "medium"}

## empathising and medium confess level
* empathise
  - action_increase_sentiment
  - slot{"sentiment": 0.6}
  - action_increase_trust
  - action_update_confess_level
  - slot{"compliance": 0.8}
  - slot{"confess_level": "high"}


## asking about accomplices success
* ask_accomplices
  - slot{"confess_level": "high"}
  - slot{"confessed": true}
  - utter_confess_accomplices

## asking about accomplices success 2
* ask_accomplices
  - slot{"confess_level": "high"}
  - slot{"confessed": false}
  - utter_confess
  - action_confess
  - slot{"confessed": true}
  - utter_confess_accomplices

## asking about accomplices failure and already confessed
* ask_accomplices
  - slot{"confess_level": "medium"}
  - slot{"confessed": true}
  - utter_protect_accomplices

## asking about accomplices failure and not confessed
* ask_accomplices
  - slot{"confess_level": "medium"}
  - slot{"confessed": false}
  - utter_deny

## asking about accomplices not confessed
* ask_accomplices
  - slot{"confess_level": "low"}
  - utter_deny
