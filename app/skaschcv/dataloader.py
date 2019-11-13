# -*- coding: utf-8 -*-
"""
The dataloader module.

Load data for the website.

Created by Romain Mondon-Cancel on 2019-11-08 22:06:08
"""

import os

import yaml

from skaschcv import textprocessor as tp


def key_for(filename: str) -> str:
    if "." not in filename:
        return filename
    return filename[: filename.rfind(".")]


def read_data(locale: str, default_locale: str):
    """
    Read the data from json file.
    """
    root_folder = os.path.dirname(os.path.dirname(__file__))
    structure_dir = os.path.join(root_folder, "config", "structure")
    text_dir = os.path.join(root_folder, "config", "text")
    static_dir = os.path.join(root_folder, "static")
    files = os.listdir(structure_dir)
    data = {}
    for filename in files:
        with open(os.path.join(structure_dir, filename), "rb") as f:
            struct_yml = f.read().decode("utf-8")
        try:
            with open(os.path.join(text_dir, filename), "rb") as f:
                text_data = yaml.safe_load(f)
        except FileNotFoundError:
            text_data = {}
        processor = tp.Processor(locale, text_data, default_locale)
        key = key_for(filename)
        data[key] = yaml.safe_load(processor(struct_yml))
        css_file = f"{key}.css"
        if css_file in os.listdir(static_dir):
            data[key]["meta"]["css"] = css_file
    return data
