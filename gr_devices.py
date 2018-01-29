# encoding: utf-8
from __future__ import unicode_literals

import codecs
import json
import re

import pyparsing as pp

import onto_data as od


# device subgrammars
with codecs.open('device_data.json', 'r', 'utf-8') as f:
    mapper = json.load(f, 'utf-8')
concept_subgrs = [pp.Regex(mapper[cpt], flags=re.IGNORECASE)(u'device:{0}'.format(cpt)) for cpt in mapper.keys()]

# phone plurals subgrammars (e.g. 'Galaxies') from onto_data.py
phone_plurals_subgrs = []
for canon_cpt in od.phone_plurals.keys():
    phone_plurals_subgrs.append(
        pp.Or(
            [pp.CaselessLiteral(cpt) for cpt in od.phone_plurals[canon_cpt]]
        )(u'device:{0}'.format(canon_cpt))
    )

# general device subgrammars (e.g. 'Router') from onto_data.py
general_device_subgrs = []
for canon_cpt in od.general_device_concepts.keys():
    general_device_subgrs.append(
        pp.Or(
            [pp.CaselessLiteral(cpt) for cpt in od.general_device_concepts[canon_cpt]]
        )(u'device:{0}'.format(canon_cpt))
    )

concept_subgrs += phone_plurals_subgrs
concept_subgrs += general_device_subgrs
devices = pp.Or(concept_subgrs)

if __name__ == '__main__':
    devices.parseString("iPhone 7")
    devices.parseString("iPhone 7S Plus 32 GB schwarz")
    devices.parseString("Speedport W921 V")
    devices.parseString("iPhone")
    devices.parseString("Galaxy")
    devices.parseString("Galaxies")
    devices.parseString("iPhones")
    devices.parseString("Smartphones")

