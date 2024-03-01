# bored-api-python
A Python script accessing the Bored API. Runnable under Python 2.7 and Python 3.x.

I provide two versions. With the `translate` Module and without.

You can use the Azure AI Translator from Microsoft, Translate from MyMemory or LibreTranslate to translate in any language. But you may have to register with one of these providers in order to use the translation. MyMemory is used by default and is the free version. Better results can be achieved by registering.

Bored API otherwise only returns English results by default.

The programme code even contains fixed translations for the categories in German, English, French and Spanish. This is not translated by the Translator because it would otherwise take longer for the result to be returned. Nothing changes in the categories and each translation could otherwise lead to different results.

Further Informations to the `translate` Module you can finde [here](https://translate-python.readthedocs.io/en/latest/index.html) and about the Bored API you can find [here](http://www.boredapi.com/).


## Pre-Installation

You can choose to install for Python 2.7 with

```
python -m pip install requests
```

or Python 3.x:

```
python3 -m pip install requests
```

And if you want to use it with the `translate` Module you can install:

```
python -m pip install requests
python -m pip install translate # currently no working version for Python 2.7
```

or Python 3.x:

```
python3 -m pip install requests
python3 -m pip install translate
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
DIFFERENT ERRORS! Beacuse currently not working.
```

What you need to bear in mind: Every request to Bored API returns different results. You can see that the results for English and German have been completely regenerated here. Since the `translate` module is already installed, if you want to have the same result translated in several languages, you could rewrite the programme and perform several translations in the main method. For me, this is not desirable as I want to generate random results each time.
