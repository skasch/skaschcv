#!/usr/bin/env python
# encoding: utf-8
"""
Creates the Flask object app to serve skaschcv.

@author: skasch
"""

import os
import typing as t

import flask
import yaml

from skaschcv import dataloader as dl

app = flask.Flask(__name__)

app.config.from_object("config")
app.config.from_envvar("SKASCHCV_SETTINGS", silent=True)

DEFAULT_LOCALE = os.environ.get("SKASCHCV_DEFAULT_LOCALE", "en-US")


def get_default_locale(host: str) -> str:
    localization_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "config", "localization.yml"
    )
    try:
        with open(localization_file, "rb") as f:
            localization = yaml.safe_load(f)
        return localization.get(host, DEFAULT_LOCALE)
    except FileNotFoundError:
        return DEFAULT_LOCALE


DEFAULT_RESUME = os.environ.get("SKASCHCV_DEFAULT_RESUME", "general")


def get_resume_data(
    request: flask.Request, resume: str = DEFAULT_RESUME, locale: str = None
) -> t.Dict:
    """
    Show the given resume.
    """
    if locale is None:
        locale = get_default_locale(request.headers["Host"])
    try:
        data = dl.read_data(locale, DEFAULT_LOCALE)[resume]
    except KeyError:
        flask.abort(404)
    return data


@app.route("/")
@app.route("/<resume>/")
@app.route("/<locale>/<resume>/")
def show_resume(resume: str = DEFAULT_RESUME, locale: str = None):
    """
    Show the given resume.
    """
    data = get_resume_data(flask.request, resume, locale)
    return flask.render_template("cv.jinja", data=data)
