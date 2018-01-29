# HackathonNLU
Simple NLU for DT Hackathon/ontology challenge

## Example utterances

* Smartphones mit Fingerabdrucksensor (intent: get_entities)
* In welchen Farben gibt es das Samsung Galaxy S6 (intent: get_options)
* Arbeitsspeicher des iPhone 7 (intent: get_attribute)
* ja/nein (intent: yes_no)

## Coverage

The NLU understands a limited number of sentences of the above types for the following parts of the domain:
* Smartphones, 
* Routers, 
* and their attributes

## Usage

\# encoding: utf-8

from nlu import NLU

user_query = "Smartphones mit Fingerabdrucksensor"

logfile = 'logs.txt'

nlu = NLU(logfile)

r = nlu.parse(user_query)

## Recognition result

import json

print json.dumps(r, indent=4)

Returns a dictionary like this:

{
    "intent": "get_entities", 
    "entities": [
        {
            "type": "device", 
            "value": "Smartphone", 
            "literal": "Smartphones"
        }, 
        {
            "type": "attribute_value_specification", 
            "value": [
                {
                    "type": "attribute", 
                    "value": "Fingerprint sensor", 
                    "literal": "Fingerabdrucksensor"
                }
            ], 
            "literal": "n.a."
        }
    ]
}

Entities have a 
* type (e.g. 'device'), which describes the type of attribute
* value (e.g. 'Smartphone' or 'Galaxy S6'), which gives the name of the object as used in the ontology
* literal, which gives the string recognized in the user query for this entity (This is not returned for composite entities attribute_value_specification)

The attribute_value_specification entity is a composite entity which can describe more complex relations such as in "mehr als 2 LAN-Anschlüsse", which would return the following dictionary:

{
    "type": "attribute_value_specification", 
    "value": [
        {
            "type": "amount", 
            "value": "2", 
            "literal": "2"
        }, 
        {
            "type": "operator", 
            "value": "gt", 
            "literal": "mehr als"
        }, 
        {
            "type": "attribute", 
            "value": "Number of Ethernet ports", 
            "literal": "LAN-Anschlüsse"
        }
    ], 
    "literal": "n.a."
}

# Code structure

Python files starting with 'gr_' contain (sub)grammars for device names, attribute names and values (incl. attribute_value_specification) and the main grammar.

onto_data.py and device_data.json contain lists of devices and attributes and some mappings to surface forms.

nlu.py defines a NLU class providing a simple interface to the grammar parser.
