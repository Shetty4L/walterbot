## say hello
* greet
  - utter_greet

## interrogate success
* ask_confession 
  - utter_deny
* threaten
  - utter_confess
* praise
  - utter_thanks

## interrogate success 2
* ask_confession 
  - utter_deny
* good_offer
  - utter_confess
* praise
  - utter_thanks

## interrogate failure 2
* ask_confession 
  - utter_deny
* bad_offer
  - utter_deny
* give_up
  - utter_gloat
  - utter_goodbye

## interrogate failure
* ask_confession 
  - utter_deny
* give_up
  - utter_gloat
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye