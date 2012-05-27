#! /usr/bin/env python3

import sqlite3
import os
import re
import sys

from time import localtime, strftime
from mako.template import Template

backup = '~/Library/Application Support/MobileSync/Backup/9540a0037afee6a5f9f7820b42c2e83b74b4e271'

sms = os.path.expanduser(os.path.join(backup, '3d0d7e5fb2ce288813306e4d4636395e047a3d28'))
addressbook = os.path.expanduser(os.path.join(backup, '31bb7ba8914766d4ba40d6dfb6113c8b614be442'))

# call history file
# call = '2b2b0084a1bc3a5ac8c27afdf14afb42c61a19ca'
# SELECT address, date, duration, flags FROM call

# Below numbers are considered as same
# +8612345678901
# +86-123-4567-8901
# 123-4567-8901
# 1 (234) 567-8901
def normalize(address):
    return ''.join(re.findall('(\d)', address))[-11:]

def fetchall(database, query):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(query)
    return cur.fetchall()


contacts = {}
for value, first, last in fetchall(addressbook, 'SELECT value, First, Last FROM ABMultiValue as v, ABPerson as p WHERE v.record_id = p.ROWID AND v.property = 3'):
    contacts[normalize(value)] = last + first

groups = {}
for address, date, text, flags in fetchall(sms, 'SELECT address, date, text, flags FROM message'):
    address = normalize(address)
    assert address
    conversation = (strftime('%Y-%m-%d %H:%M:%S %a', localtime(date)), text, flags)
    if address in groups:
        groups[address].append(conversation)
    else:
        groups[address] = [conversation]

rendered_html = Template(open('viewer.html').read()).render(contacts=contacts, groups=groups)
print('Content-Type: text/html\r\n\r\n' + rendered_html)

