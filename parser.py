#!/usr/bin/python
''' Warning: 
Regular expressions passing on the command line, there shouldn't be any 
string that matches against two or more Regex.

Example:

    +-----------------------------------------------------------------+
    |                                                                 |
    |   Welcome to our website!                                       |
    |                                                                 |
    |   2010.09.09                                                    |
    |        I created this parser                                    |
    |                                                                 |
    |   2010.09.10                                                    |
    |        Hang over! arggh                                         |
    |                                                                 |
    |                             Last activity: 2010.09.09 12:27 P.M |
    |   About|Contact|....                                            |
    +-----------------------------------------------------------------+

Let's say you want to extract my activity information from this site.

Then you need to pass following regex elements as arguments:

    "\d{4}.\d{2}.\d{2}" ".{10,}"

Even if this parser finds the text, it won't return the captured elements.
Use named group to retrieve them.

    "(?P<Day>\d{4}.\d{2}.\d{2})" "(?P<Activity>.{10,})" or more explicitly:
    "(?P<Day>\d{4}.\d{2}.\d{2})$" "(?P<Activity>.{10,})" 

'''
import sys
import re
import optparse

def fix_whitespaces(text):
    return re.sub(r'\s+', ' ', text)

def print_dict(d):
    print fix_whitespaces(','.join([ '%s' % (v) for k, v in d.iteritems() ]))

def break_text(html, trim=True):
    ' >.< '
    breaker = re.compile(r'>(.*?)<', re.S)
    for m in breaker.finditer(html):
        yield m.group(1).strip()

def all_elements(texts, args):
    args = [ unicode(a, 'utf8') for a in args ]
    args_count = len(args)
    captures = { }
    enum = enumerate(args)
    for text in texts:
        text = unicode(text, 'utf8')
        for i, arg in enum:
            m = re.match(arg, text, re.I|re.U|re.S)
            if m:
                captures.update(m.groupdict())
                if i == args_count-1: 
                    yield captures
                else:
                    break
        else:
            enum = enumerate(args)

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-i', '--input', dest='input_stream', action='store', help='Sets input stream. "-" to standard input, or filename')
    (options, args) = parser.parse_args()
    if not options.input_stream:
        parser.error('-i is required option, please specify input.')
    if not args:
        parser.error('No element specified, please specify one or more elements to extract.')
    element_specs, fn = args, options.input_stream
    fd = (fn == '-') and sys.stdin_stream or open(fn, 'r')
    texts = break_text(fd.read())
    for text in all_elements(texts, element_specs):
        print_dict(text)

