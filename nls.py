# -*- coding: utf-8 -*-

import os
import openai
import click
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """
Eingabe: Dateien auflisten
Ausgabe: ls -l

Eingabe: Zähle Dateien im Ordner
Ausgabe: ls -l | wc -l

Eingabe: Speicherplatz verbraucht durch Nutzerordner
Ausgabe: du ~

Eingabe: Ersetze foo mit bar in allen .py Dateien
Ausgabe: sed -i .bak -- 's/foo/bar/g' *.py

Eingabe: Lösche den models Odner
Ausgabe: rm -rf ./models"""

template = """

Eingabe: {}
Ausgabe:"""

try:
    while True:
        request = input(click.style("nlsh> ", "red", bold=True))
        prompt += template.format(request)
        result = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            stop="\n",
            max_tokens=100,
            temperature=0.0,
        )
        command = result.choices[0]['text']
        prompt += command

        if click.confirm(f">>> Run: {click.style(command, 'blue')}", default=True):
            os.system(command)
except KeyboardInterrupt:
    pass