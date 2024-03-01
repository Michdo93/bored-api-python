# bored-api-python
A Python script accessing the Bored API. Runnable under Python 2.7 and Python 3.x.

The tranlation file uses an `Google Translator` endpoint for translation.


## Pre-Installation

You can choose to install for Python 2.7 with

```
python -m pip install requests
```

or Python 3.x:

```
python3 -m pip install requests
```

## Usage

You have to run:

```
python bored_api.py
```

As example you will receive:

```
BUSYWORK: Create or update your resume
EDUCATION: Research a topic you're interested in
RECREATIONAL: Go to the gym
SOCIAL: Catch up with a friend over a lunch date
DIY: Find a DIY to do
CHARITY: Contribute code or a monetary donation to an open-source software project
COOKING: Create a meal plan for the coming week
RELAXATION: Take a bubble bath
MUSIC: Learn to play a new instrument
```

Or you can run the version with translate.

```
python bored_api_translate.py
```

As example you will receive:

```
Gehen Sie mit ein paar Freunden auf ein Musikfestival
Lernen Sie eine neue Programmiersprache
Lernen Sie Eislaufen oder Rollschuhlaufen
Treffen Sie sich bei einem Mittagessen mit einem Freund
Repariere etwas, das in deinem Haus kaputt ist
Sammle Müll in deinem Lieblingspark ein
Machen Sie selbstgemachtes Eis
Beginnen Sie mit einem Buch, zu dessen Lektüre Sie noch nie gekommen sind
Gründe eine Band
Konfigurieren Sie die Zwei-Faktor-Authentifizierung für Ihre Konten
```

What you need to bear in mind: Every request to Bored API returns different results. You can see that the results for English and German have been completely regenerated here.
