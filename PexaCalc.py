import sys, subprocess

try:
    from requests import get
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    from requests import get
try:
    import json
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "json"])
    import json
try:
    from decimal import Decimal
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "decimal"])
    from decimal import Decimal
try:
    from appJar import gui
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "appJar"])
    from appJar import gui
try:
    from pyperclip import copy
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
    from pyperclip import copy



r = get('https://api.freiexchange.com/public/PEXA')
a = r.json()['PEXA_BTC']

for dictionary in a:
    try:
        #print(dictionary['low'])
        low = dictionary['low']
        high = dictionary['high']
        last = dictionary['last']
    except KeyError:
        pass

def calc():
    b = float(app.getEntry('Pexa'))
    value = Decimal((b * float(low)))
    value = round(value, 8)
    print (str(value))
    app.setLabel('val', text=(str(b) + " PEXA is worth " + str(value) + "BTC"))

def donate():
    copy('x1qlhvx2843rm9muqg647r8py48qvk75jydhgnpx7')
    app.setLabel('copied', text="Address Copied!!")

app = gui("PEXA Calculator")
app.addLabel('Values are from Freiexchange')
app.addLabel("Values: " + "High: " + str(high) + " Low: " + str(low) + " Last: "+ str(last))
app.addNumericEntry('Pexa')
app.addButton("Calculate", calc)
app.addLabel('val', text="")
app.addButton('Donate Pexa', donate)
app.addLabel('copied', text="If you would like to donate, click the 'Donate Pexa' button to copy address")
app.go()
