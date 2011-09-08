#!/usr/bin/python
'''
This is a simple command line based HTML parser. 

You should specify regular expessions as entity. Let's say E. 

E1 ---> E2 ---> E3 ---> E4

It will try to search E1, and then E2, and E3 ... etc. 
'''
import sys
import re
# E1 ---> E2 ---> E3

def print_dict(d):
    print ', '.join([ '%s:%s' % (k, v) for k, v in d.iteritems() ])

def break_text(html, trim=True):
    ' >.< '
    breaker = re.compile(r'>(.*?)<', re.S)
    for m in breaker.finditer(html):
        yield m.group(1).strip()

def all_elements(texts, args):
    args = [ unicode(a, 'utf8') for a in args ]
    captures = [ ]
    for text in texts:
        text = unicode(text, 'utf8')
        for i, arg in enumerate(args):
            m = re.match(arg, text, re.I|re.U|re.S)
            if m:
                yield i, m.groupdict()
                break

if __name__ == '__main__':
    fn, element_specs = sys.argv[1], sys.argv[2:]
    with open(fn) as f:
        texts = break_text(f.read())
        last_index = 0
        captured_indexes = [ ]
        captures = { }
        for index, text in all_elements(texts, element_specs):
            if index == len(element_specs)-1:
                captures.update(text)
                print_dict(captures)
            else:
                captures.update(text)
            captured_indexes.append(index)
            last_index = index

