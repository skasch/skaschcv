# -*- coding: utf-8 -*-
"""
The textprocessor module.

Contain functions to process text content.

Created by Romain Mondon-Cancel on 2019-11-08 21:18:21
"""

import re
import logging
import sys
import typing as t

logger = logging.getLogger(__name__)
logging_formatter = logging.Formatter(
    "%(asctime)s | %(name)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
logging_handler = logging.StreamHandler(sys.stdout)
logging_handler.setFormatter(logging_formatter)
logger.addHandler(logging_handler)
logger.setLevel(logging.INFO)


class Processor:
    def __init__(self, locale: str, text_data: t.Dict, default_locale: str = "en-US"):
        """
        Processor to update localized text data in structure data.

        Args:
            locale: The locale to use.
        """
        self.locale = locale
        self.text_data = text_data
        self.default_locale = default_locale

    def replacer(self, match: t.Match) -> str:
        """
        Replace a name tag by the actual value of that tag from ``self.text_data``.

        Args:
            string: The string to process.

        Returns:
            The content of the string from ``self.text_data`` based on the locale.
        """
        string = match.group()
        left = string.rfind("{") + 1
        right = string.find("}") - 1
        tags = [tag.strip() for tag in string[left:right].strip().split(".")]
        res = self.text_data
        for tag in tags:
            try:
                res = res[tag]
            except KeyError:
                raise ValueError(f"Invalid string tag {'.'.join(tags)}.")
        return str(res.get(self.locale, res[self.default_locale]))

    def __call__(self, structure_string: str) -> str:
        """
        Process a structure string by replacing text tags by localized values.

        Args:
            structure_string: The string representing the structure data.

        Returns:
            The processed string with the text tags replaced.
        """
        res = re.sub(r'"?{{[\w\s.]*}}"?', self.replacer, structure_string, flags=re.M)
        return res
