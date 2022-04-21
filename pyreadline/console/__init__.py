from __future__ import print_function, unicode_literals, absolute_import
import glob, sys

success = False
in_ironpython = "IronPython" in sys.version

try:
    if in_ironpython:
        from .ironpython_console import *
    else:
        from .console import *
    success = True
except ImportError:
    raise
if not success:
    raise ImportError(
            "Could not find a console implementation for your platform")
