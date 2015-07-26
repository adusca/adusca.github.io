import ijson.backends.yajl2 as ijson
import json


def load_json(filename):
    with open(filename, 'r') as fd:
        parser = ijson.parse(fd)
        ret = {'builders': {}}
        for prefix, event, value in parser:
            if (prefix, event) == ('builders', 'map_key'):
                buildername = value
                ret['builders'][buildername] = {}
            elif prefix.endswith('.shortname'):
                ret['builders'][buildername]['shortname'] = value

        return ret


def load_json2(filename):
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    load_json('allthethings.json')
