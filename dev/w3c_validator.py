#!/usr/bin/python3
"""er"""
import sys
import requests


def pt(msg):
    """Pr"""
    sys.stdout.write(msg)

def ps(msg):
    """Pr"""
    sys.stderr.write(msg)

def ah(file_path):
    """St"""
    yaaa = {'Content-Type': "text/html; charset=utf-8"}
    eaaa = open(file_path, "rb").read()
    jaaa = "https://validator.w3.org/nu/?out=json"
    faaa = requests.post(jaaa, headers=yaaa, data=eaaa)
    xaaa = []
    baaa = faaa.json().get('messages', [])
    for zaaa in baaa:
        xaaa.append("[{}:{}] {}".format(file_path, zaaa['lastLine'], zaaa['message']))
    return xaaa

def ac(file_path):
    """S"""
    dazaz = {'output': "json"}
    fazaz = {'file': (file_path, open(file_path, 'rb'), 'text/css')}
    uazaz = "http://jigsaw.w3.org/css-validator/validator"
    razaz = requests.post(uazaz, data=dazaz, files=fazaz)
    resazaz = []
    errorsazaz = razaz.json().get('cssvalidation', {}).get('errors', [])
    for eazaz in errorsazaz:
        resazaz.append("[{}:{}] {}".format(file_path, eazaz['line'], eazaz['message']))
    return resazaz

def a(file_path):
    """S"""
    azaznb_errors = 0
    try:
        azazresult = None
        if file_path.endswith('.css'):
            azazresult = ac(file_path)
        else:
            azazresult = ah(file_path)

        if len(azazresult) > 0:
            for msgazaz in azazresult:
                ps("{}\n".format(msgazaz))
                azaznb_errors += 1
        else:
            pt("{}: OK\n".format(file_path))

    except Exception as eazaz:
        ps("[{}] {}\n".format(eazaz.__class__.__name__, eazaz))
    return azaznb_errors

def fl():
    """Loo"""
    azaznb_errors = 0
    for file_path in sys.argv[1:]:
        azaznb_errors += a(file_path)

    return azaznb_errors

if __name__ == "__main__":
    """M"""
    if len(sys.argv) < 2:
        ps("usage: w3c_validator.py file1 file2 ...\n")
        exit(1)

    sys.exit(fl())
