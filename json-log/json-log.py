#!/usr/bin/env python
# AUTO generated source
import re
import os
import sys
import json
import argparse
from jinja2 import Environment


def read_template(name):
    paths = [
        os.path.join(os.path.expanduser('~/.json-log'), name),
        os.path.join(os.getcwd(), name),
        os.path.expanduser(name)]
    for path in paths:
        if os.path.exists(path):
            with open(path) as f:
                template = re.sub(
                    r'(@[a-zA-Z.]+)', r'\1@', f.read())
                return Environment(
                    variable_start_string='@',
                    variable_end_string='@').from_string(template)
    raise ValueError(
        'Template file not found in paths: {}'.format(paths))


def formatter(log_obj):
    return template.render(**log_obj.context_variables())


class Log(dict):
    def context_variables(self):
        return {k.replace('@', ''): v for k, v in self.items()}


def read_log_obj(line):
    if len(line) > 1e9:
        raise ValueError('Line is too long')
    return Log(**json.loads(line))


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", default='default.j2')
    parser.add_argument("--filter", default='')
    return parser.parse_args()


def skip_empty(it):
    for i in it:
        i = i.strip()
        if not i:
            continue
        yield i


def main():
    for line in skip_empty(sys.stdin):
        try:
            log_obj = read_log_obj(line)
        except ValueError as err:
            print("can't read line: {}".format(err), file=sys.stderr)
            continue
        if log_filter(log_obj):
            print(formatter(log_obj))


expr_parser = re.compile(r'(?P<field>^@[a-zA-Z0-9.]+)(?P<op>=|~)(?P<value>.+)')


def parse_filter(expr_str):
    
    match = expr_parser.match(expr_str)
    if not match:
        raise ValueError('Invalid filter expression')
    return match.groupdict()


operators = {
    '=': lambda a, b: a == b,
    '~': lambda a, b: b in a
}


def create_log_filter(expr):
    if not expr:
        return lambda x: True

    def wrapped(log_obj):
        try:
            return operators[expr['op']](log_obj.get(expr['field']), expr['value'])
        except (ValueError, TypeError) as err:
            print("can't filter: {}".format(err), file=sys.stderr)
            return False
    return wrapped


def getter(self, field):
    fields = field.split('.')
    vars = self
    for f in fields:
        if f in vars:
            vars = vars[f]
        else:
            raise ValueError(
                '"{}" part from "{}" not found'.format(f, field))
    return vars


Log.get = getter


if __name__ == '__main__':
    try:
        options = parse_options()
        template = read_template(options.format)
        log_filter = create_log_filter(parse_filter(options.filter))
        main()
    except Exception as err:
        print('error: {} ({})'.format(err, type(err)), file=sys.stderr)
        sys.exit(1)
