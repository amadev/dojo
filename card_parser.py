import pprint
import sys
import yaml as yml
import os


def parse(data):
    yaml = []
    exmp = []
    assert_started = False
    for l in data:
        if not l.strip() and exmp:
            break
        if l.startswith('# '):
            yaml.append(l.replace('# ', ''))
        if l.startswith('assert ') or assert_started:
            exmp.append(l)
            assert_started = True
    if yaml and 'name:' in yaml[0]:
        data = yml.load('\n'.join(yaml))
        data['example'] = '\n'.join(exmp)
        return data


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print ('"name: {name}\ninput: {input}\n'
               'output: {output}\nexample: {example}"; "idea: {idea}"').format(
                   **parse(f.readlines()))
