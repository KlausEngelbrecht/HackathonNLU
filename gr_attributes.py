# encoding: utf-8
from __future__ import unicode_literals

import pyparsing as pp
from re import IGNORECASE
import onto_data as od


# attribute subgrammars (TODO: add attribiutes for media receivers)
od_attributes = od.smartphone_attributes.copy()
od_attributes.update(od.router_attributes)
attribute_subgrs = []
for canon_cpt in od_attributes.keys():
    attribute_subgrs.append(
        pp.Or(
            [pp.CaselessLiteral(cpt) for cpt in od_attributes[canon_cpt]]
        )(u'attribute:{0}'.format(canon_cpt))
    )
attributes = pp.Or(attribute_subgrs)

var_smartphone_attributes = pp.Or([
    pp.CaselessLiteral('Speichergrößen')('attribute:{0}'.format(od.DATA_STORAGE)),
    pp.CaselessLiteral('Farben')('attribute:{0}'.format(od.COLOR))
])

# Attribute value specifications

# metric attributes
gt = pp.oneOf(['mehr als', 'über'])('operator:gt')
lt = pp.oneOf(['weniger als', 'unter'])('operator:lt')
number = pp.Word(pp.nums + '.,-+')('amount')
unit = pp.oneOf(od.units, caseless=True)('unit')
metric_specs = pp.Group(
    pp.Optional(gt) + number + pp.Optional(unit) + attributes
)
# Hersteller
make = pp.oneOf(od.makes, caseless=True)(od.MANUFACTURER)
# Betriebssystem
os_type = pp.oneOf(od.os, caseless=True)('os_name')
os_version = pp.Word(pp.nums + '.,-+')('version') # TODO: some also have names)
os_spec = pp.Group(
    pp.Optional("Betriebssystem")('attribute:{0}'.format(od.OS)) + 
    os_type + 
    pp.Optional(os_version) + 
    pp.Optional("-") + pp.Optional("Betriebssystem")('attribute:{0}'.format(od.OS))
)
# Farbe
color = pp.oneOf(od.colors, caseless=True)('value')
# SIM-Format
sim = pp.Group(
    pp.oneOf(od.sim_formats, caseless=True)('value') + 
    pp.Regex('-?SIM', flags=IGNORECASE)('attribute:{0}'.format(od.SIM_FORMAT)) + 
    pp.Optional(pp.Or(["-Karte", "-Format"]))
)
# Display-Typ
screen = pp.Group(
    pp.oneOf(od.display_type, caseless=True)('value') +
    pp.Regex('-?(Display|Bildschirm)', flags=IGNORECASE)('attribute:{0}'.format(od.DISPLAY_TYPE))
)
# Fingerprint-Sensor
fingerprint = pp.Group(
    pp.Regex('Fingerabdruck-?sensor', flags=IGNORECASE)('attribute:{0}'.format(od.FINGERPRINT_SENSOR))
)
# integrierte DECT-Basis
dect = pp.Group(
    pp.Regex('integrierter? DECT( |-)Basis', flags=IGNORECASE)('attribute:{0}'.format(od.DECT))
)
# integriertes DSL Modem
dsl = pp.Group(
    pp.Regex('integrierte(s|m) DSL( |-)Modem', flags=IGNORECASE)('attribute:{0}'.format(od.DSL))
)
# DSL-Telefonie
dsl_telephony = pp.Group(
    pp.Regex('DSL( |-)Telefon(ie|-?anschlu(ss|ß))?', flags=IGNORECASE)('attribute:{0}'.format(od.DSL_TELEPHONY))
)
# Repeater-Mode
repeater = pp.Group(
    pp.Regex('Repeater( |-)(Mod(e|us)|Funktion)', flags=IGNORECASE)('attribute:{0}'.format(od.REPEATER))
)
# USB-Typ
usb_type = pp.Group(
    pp.oneOf(od.usb_types, caseless=True)('value') +
    pp.Regex('-?USB', flags=IGNORECASE)('attribute:{0}'.format(od.USB_TYPE)) +
    pp.Optional(pp.Or(["-Anschluss", "-Anschluß", "-Anschlüssen", "-Buchse", "Buchsen"]))
)
# VDSL-kompatibel
vdsl = pp.Group(
    pp.Regex('VDSL( |-)kompatibel', flags=IGNORECASE)('attribute:{0}'.format(od.VDSL))
)
# WLAN-Standards
wifi_std = pp.Group(
    pp.oneOf(od.wifi_std, caseless=True)('value') +
    pp.Regex('-?(WiFi|WLAN)', flags=IGNORECASE)('attribute:{0}'.format(od.USB_TYPE)) +
    pp.Optional(pp.Or(["-Standard", "Verbindung"]))
)
# WLAN-Encryption
wifi_encryption = pp.Group(
    pp.oneOf(od.wifi_encryption, caseless=True)('value') +
    pp.Optional(pp.Regex('-?(WiFi|WLAN)?(( |-)Verschlüsselung)?', flags=IGNORECASE)('attribute:{0}'.format(od.USB_TYPE)))
)


# Alternative of all attribute_value_specs types
attribute_value_spec = pp.Or([
    metric_specs, make, os_spec, color, sim, screen, fingerprint, dect, dsl, dsl_telephony,
    repeater, usb_type, vdsl, wifi_std, wifi_encryption
])('attribute_value_specification')

def assert_parsable(expression):
    # This will show an informatie error message if not parsable
    attribute_value_spec.parseString(expression)



if __name__ == '__main__':
    attributes.parseString("Speichergrößen")
    attributes.parseString("WLAN-Standards")
    attributes.parseString('integrierte DECT-Basis')
    attributes.parseString("Anzahl Ethernet-Anschlüsse")
    attribute_value_spec.parseString("mehr als 16 GB Arbeitsspeicher")
    attribute_value_spec.parseString(u"mehr als 100 GB Speichergröße")
    attribute_value_spec.parseString("mehr als 2 LAN-Anschlüssen")
