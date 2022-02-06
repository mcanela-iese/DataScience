## Tutorial - String data in Python ##

# Strings as lists #
iese = 'IESE Business School'
len(iese)
iese[5:]
iese[:4] + ', A way to learn'
'IE' in iese

# Python string functions #
iese.lower()
iese.replace('IESE', 'Iese')
iese.split(' ')
iese.split('i')
iese.find('Business') 
iese.find('Negocios')
iese.count('s')

# Regular expressions #
import re
re.sub('[a-z]', 'x', iese)
re.sub('[a-z]+', 'x', iese)
re.split('\W+', 'IESE: A way to learn, a mark to make')
re.findall('\w+', iese)

# Pandas string functions #
import pandas as pd
pres = pd.Series(['Donald Trump', 'Joe Biden', '', None])
pres
pres.str.len()
pres.str.lower()
bio = pd.Series(['I was born in 1954', 'My phone is +34 932 534 200'])
bio.str.replace('[0-9]', 'x', regex=True)
bio.str.contains('\+[0-9]{2} [0-9]{3} [0-9]{3}', regex=True)
