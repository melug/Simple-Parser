#!/bin/bash

./parser.py -i gogo_horoscope.html ".*?(?P<ZodiacSign>хонь|хамтатгах|жинлүүр|хилэнц|нум|матар|хумх|загас|мэлхий|арслан|үхэр|охин)" "(?P<Horoscope>[^.][^{}]{100,})"

./parser.py -i olloo_example.html "(?P<Currency>USD|EUR|JPY|CHF|SEK|GBP|CNY|RUB|KRW)" "(?P<Rate>\d+.\d+)$"

./parser.py -i tv.html "(?P<WeekDay>\w+) гараг" "\-(?P<TvName>[\w ]+) телевиз -" "(?P<Time>\d{2}[:.]\d{2})" "(?P<ProgramName>.{5,})"

./parser.py -i golomt.html "(?P<Currency>USD|CNY|EUR|JPY|GBP|CHF|RUR|KRW|HKD|AUD|CAD|SGD|SEK|XAU|XAG)" "(?P<MongolBank>[\d,.]+)$"
