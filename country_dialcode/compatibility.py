from past.builtins import basestring
import sys


PY2 = sys.version_info[0] == 2
if not PY2:
    text_type = str
    binary_type = bytes
    string_types = (str,)
    integer_types = (int,)
else:
    text_type = str
    binary_type = str
    string_types = basestring
    integer_types = (int, int)
