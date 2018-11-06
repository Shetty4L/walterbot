## say hello
* greet
  - utter_greet

## asking for confession
* ask_confession
  - utter_deny

## threaten suspect
* threaten
  - utter_confess

## interrogate success
* ask_confession 
  - utter_deny
* threaten
  - utter_confess
* praise
  - utter_thanks

## give offer
* give_offer {"offer": "2"}
  - action_calculate_compliance
  - slot{"compliance": 0.1}
  - action_update_confess_level
  - slot{"confess_level" : "low"}
  - utter_deny

## give offer 2
* give_offer
  - action_calculate_compliance
  - slot{"compliance": 0.6}
  - action_update_confess_level
  - slot{"confess_level" : "medium"}
  - utter_confess

## give offer 3
* give_offer {"offer": "10"}
  - action_calculate_compliance
  - slot{"compliance": 0.8}
  - action_update_confess_level
  - slot{"confess_level" : "high"}
  - utter_confess
  - utter_confess_details

## interrogate failure
* ask_confession 
  - utter_deny
* give_up
  - utter_gloat
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## Generated Story 8702501571408614427
* give_offer {"offer": "5"}
    - slot{"offer": "5"}
    - action_calculate_compliance
    - slot{"compliance": 0.3}
    - action_update_confess_level
    - slot{"confess_level": "low"}
    - utter_deny
* give_offer {"offer": "5"}
    - slot{"offer": "7"}
    - action_calculate_compliance
    - slot{"compliance": 0.6}
    - action_update_confess_level
    - slot{"confess_level": "medium"}
    - utter_confess
* give_offer {"offer": "8"}
    - action_calculate_compliance
    - slot{"compliance": 0.9}
    - action_update_confess_level
    - slot{"confess_level": "high"}
    - utter_confess
    - utter_confess_details

