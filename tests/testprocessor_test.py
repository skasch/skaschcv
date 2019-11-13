#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test for the testprocessor_test module.

Created by Romain Mondon-Cancel on 2019-11-08 21:45:54
"""

from skaschcv import textprocessor as tp


test_yml = """
data:
    foo: "{{ bar.key }}"
    bar: Hello
meta:
    baz: "{{ hello.world }}"
"""

expected_yml = """
data:
    foo: "Réussite !"
    bar: Hello
meta:
    baz: "Default replacement"
"""

text_data = {
    "bar": {"key": {"en-US": "Success!", "fr-FR": "Réussite !"}},
    "hello": {"world": {"en-US": "Default replacement"}},
}

test_locale = "fr-FR"


def testprocessor_test():
    processor = tp.Processor(test_locale, text_data)
    processed_yml = processor(test_yml)
    assert processed_yml == expected_yml
