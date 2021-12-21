## Example - Skills requested in Google job posts ##

# Importing the data #
import pandas as pd
url = 'https://raw.githubusercontent.com/mcanela-iese/DataScience/main/Data/google.csv'
df = pd.read_csv(url)
df.info()
df.head()

# Duplicated job posts #
df.duplicated().sum()
df = df.drop_duplicates()
df.info()

# Exploring the company #
df['company'].value_counts()

# Exploring the job title #
len(df['title'].value_counts())
df['title'].value_counts().head(10)
mask1 = df['title'].str.contains('Intern')
mask1.value_counts()
mask1 = df['title'].apply(lambda x: 'Intern' in x)
mask2 = ['Intern' in x for x in df['title']]
df['title'].str.contains('Sales').sum()
df['title'].str.contains('Cloud').sum()
df['title'].str.contains('Google Cloud').sum()

# Exploring the category #
len(df['category'].value_counts())
df['category'].value_counts().head(10)

# Exploring the location #
country = df['location'].str.replace(pat='.+, ', repl='', regex=True)
len(country.value_counts())
country.value_counts().head(10)

# Exploring the last three columns #
df[df['responsibilities'].isna() | df['minqual'].isna() | df['prefqual'].isna()]
df = df.dropna()
df['responsibilities'].str.len().min()
df['minqual'].str.len().min()
df['prefqual'].str.len().min()

# Analysis of the preferred qualifications #
prefqual = df['prefqual'].str.lower()
prefqual[0]
import re
bags = [re.findall('\w+', p) for p in prefqual]
len(bags[0])
bags[0][:10]
terms = [t for b in bags for t in b]
len(terms)
pd.Series(terms).value_counts().head(10)
url = 'https://raw.githubusercontent.com/mcanela-iese/DataScience/main/Data/stopwords.csv'
stopwords = pd.read_csv(url, header=None, squeeze=True)
stopwords.shape
stopwords = stopwords.tolist()
terms = [t for t in terms if t not in stopwords]
len(terms)
pd.Series(terms).value_counts().head(10)
prefqual.str.contains('experience').mean().round(3)
prefqual.str.contains('ability').mean().round(3)
prefqual.str.contains('skills').mean().round(3)
prefqual.str.contains('management').mean().round(3)
prefqual.str.contains('communication').mean().round(3)
prefqual.str.contains('pyhton').mean().round(3)
