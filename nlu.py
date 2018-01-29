# encoding:utf-8
from __future__ import unicode_literals

import json
import codecs
from collections import OrderedDict
from copy import deepcopy
import pyparsing as pp

from gr_main import main


class NLU:
    def __init__(self, logfile=False):
        self.logfile = logfile
        self.none_result = OrderedDict(
            [('intent', 'None'), ('entities', [])]
        )

    def parse(self, query):
        try:
            r = main.parseString(query)
        except (pp.ParseException, pp.ParseFatalException):
            result = deepcopy(self.none_result)
        else:
            print json.dumps(r.asDict(), indent=4)
            result = self.convert_result(r.asDict())
        if self.logfile:
            self.log(query, result)
        return result

    def log(self, query, result):
        with codecs.open(self.logfile, 'a', 'utf-8') as f:
            f.write(
                '\n' + query + '|' + json.dumps(result, ensure_ascii=False)
            )

    def convert_result(self, parse_result):
        nlu_result = deepcopy(self.none_result)
        keys = parse_result.keys()
        if len(keys) != 1:
            return nlu_result
        nlu_result['intent'] = keys[0]
        ents = parse_result[nlu_result['intent']]
        if not isinstance(ents, dict):
            return nlu_result
        for key in ents.keys():
            entity = OrderedDict()
            pair = key.split(':')
            if key == 'attribute_value_specification':

                entity['type'] = key
                entity['value'] = self.convert_result({key: ents[key]})['entities']
                entity['literal'] = 'n.a.'
            elif len(pair) == 1:
                entity['type'] = key
                entity['value'] = ents[key]
                entity['literal'] = ents[key]
            elif len(pair) == 2:
                entity['type'] = pair[0]
                entity['value'] = pair[1]
                entity['literal'] = ents[key]
            else:
                continue
            nlu_result['entities'].append(entity)
        return nlu_result


if __name__ == '__main__':
    nlu = NLU('logs.txt')
    r = nlu.parse("Gibt es das Speedport mit mehr als 2 LAN-Anschlüssen")
    print json.dumps(r, indent=4)