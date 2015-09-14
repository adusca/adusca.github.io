import json

KEYS_TO_COUNT = ['failure', 'exception', 'retry', 'success', 'cancelled', 'warnings', 'value']


def process(node):
    if 'children' in node:
        for son in node['children']:
            process(son)
            for key in KEYS_TO_COUNT:
                node[key] = node.get(key, 0) + son[key]


with open('dados.json', 'r') as f:
    a = json.load(f)

process(a)

with open('dados2.json', 'w') as f:
    json.dump(a, f, indent=4)
