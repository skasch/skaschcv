#!/usr/bin/env python
# encoding: utf-8
"""
Run the Flask application skaschcv.

@author: skasch
"""

import os

from skaschcv import app

port = int(os.environ.get("SKASCHCV_PORT", "5000"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
