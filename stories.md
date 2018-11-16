## say hello
* greet
  - utter_greet

## asking for confession high level
* ask_confession
  - slot{"confess_level" : "high"}
  - utter_confess
  - action_confess

## asking for confession medium level
* ask_confession
  - slot{"confess_level" : "medium"}
  - utter_confess
  - action_confess

## asking for confession low level
* ask_confession
  - slot{"confess_level" : "low"}
  - utter_deny

## give bad offer
* give_offer {"offer": "2"}
  - action_update_confess_level
  - slot{"confess_level" : "low"}
  - utter_deny

## give ok offer 
* give_offer {"offer": "5"}
  - action_update_confess_level
  - slot{"confess_level" : "medium"}
  - utter_confess
  - action_confess

## give offer high
* give_offer {"offer": "10"}
  - action_update_confess_level
  - slot{"confess_level" : "high"}
  - utter_confess
  - action_confess

## say goodbye
* goodbye
  - utter_goodbye

## threatening
* threaten_suspect
  - action_increase_fear
  - action_update_confess_level

## threatening family
* threaten_family
  - action_increase_anger
  - action_decrease_sentiment
  - action_decrease_trust
  - action_update_confess_level

## reassuring
* reassure
  - action_increase_trust
  - action_increase_sentiment
  - action_update_confess_level

## judging
* judge
  - action_increase_anger
  - action_decrease_sentiment
  - action_update_confess_level

## make guilty
* evoke_guilt
  - action_increase_guilt
  - action_update_confess_level

## empathising
* empathise
  - action_increase_sentiment
  - action_increase_trust
  - action_update_confess_level

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


