#!/usr/bin/env python3

import cgi
import os


form = cgi.FieldStorage()
email = form.getfirst('email', 'не задано')

# os.system(f'python3 sender.py')

print("Content-type: text/html; charset=utf-8\n")
print(f'<p>На вашу почту {email} отправлено письмо. Пожалуйста подтвердите его.</p>')
