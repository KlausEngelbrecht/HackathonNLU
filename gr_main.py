# encoding:utf-8
from __future__ import unicode_literals

from re import IGNORECASE

import pyparsing as pp

from gr_devices import devices
from gr_attributes import attributes, var_smartphone_attributes, attribute_value_spec

yes_no = pp.Group(pp.Or([
    pp.oneOf(['ja', 'jo', 'jupp', 'OK'], caseless=True)('yes_no:yes'),
    pp.oneOf(['nein', 'nee', 'nö'], caseless=True)('yes_no:no')
])).setResultsName('yes_no')

devices_and_attributes = pp.Or([
    pp.Group(
        attributes + pp.Or(["des", "vom", "beim"]) + devices
    ).setResultsName('get_attribute'),
    pp.Group(
        pp.Regex('Hat (das|der|die)', IGNORECASE) + devices + pp.Regex('eine?n?') + attributes
    ).setResultsName('get_attribute'),
    pp.Group(
        pp.Regex('Ist (das|der|die)', IGNORECASE) + devices + attributes
    ).setResultsName('get_attribute'),
    pp.Group(
        pp.oneOf(["Mit", "In"], caseless=True) + "welchen" + attributes + "gibt es das" + devices
    ).setResultsName('get_options'),
    pp.Group(
        devices + pp.oneOf(["mit", "in", "von"]) + attribute_value_spec
    ).setResultsName('get_entities')
])

main = pp.Or([
    pp.SkipTo(devices_and_attributes) + devices_and_attributes,
    yes_no
])



if __name__ == '__main__':
    main.parseString("In welchen Speichergrößen gibt es das iPhone7")
    main.parseString("Arbeitsspeicher des Sony XperiaXZ Premium")
    main.parseString("iPhone 7 mit mehr als 16 GB Arbeitsspeicher")
    main.parseString("iPhone 7 mit Fingerabdrucksensor")
    main.parseString("iPhone 7 mit mehr als 100 GB Speichergröße")
    main.parseString("WLAN-Standards des Speedport W 921V")
    main.parseString("Hat das Speedport W 921V eine integrierte DECT-Basis")
    main.parseString("Anzahl Ethernet-Anschlüsse des Speedport W 921 V")
    main.parseString("iPhone7 mit mehr als 2 Anzahl Ethernet-Anschlüsse")
    main.parseString("Ist das Speedport W 921V VDSL-kompatibel")
