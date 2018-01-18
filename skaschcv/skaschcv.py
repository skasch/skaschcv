#!/usr/bin/env python
# encoding: utf-8
"""
skaschcv.py

Created by Romain Mondon-Cancel on 2018-01-18.
"""
import json
import io
from flask import Flask, g, render_template

app = Flask(__name__)
app.config.from_object(__name__)

# app.config.update(dict())
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def read_data():
    """
    Read the data from json file.
    """
    with app.open_resource('json/data.json', mode='rb') as json_file:
        json_content = json_file.read().decode('utf-8')
        return json.loads(json_content)


def get_data(endpoint):
    """
    Read the json data if not loaded yet for the current application context.
    """
    if not hasattr(g, 'json_data'):
        g.json_data = list(filter(lambda x: x['endpoint'] == endpoint,
                                  read_data()))[0]['data']
        print(g.json_data['header']['description'])
    return g.json_data

@app.route('/')
def show_resume():
    """
    Show the default resume.
    """
    endpoint = '/'
    data = get_data(endpoint)
    return render_template("cv.html", data=data)
