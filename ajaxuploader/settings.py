"""
Any of the settings below can be easily overridden in the project settings
by simply defining a value with the PREFIX included in its name.
e.g. AJAXUPLOADER_UPLOAD_DIRECTORY = 'uploads/images'
"""

import os
import sys
from django.conf import settings

PREFIX = 'AJAXUPLOADER_'
DEFAULT_SETTINGS = {
    'UPLOAD_DIRECTORY': os.path.join('uploads', 'ajax'),
    }

def prefixed(string):
    return '%s%s' % (PREFIX, string)

for name, default in DEFAULT_SETTINGS.items():
    setattr(sys.modules[__name__], name,
            getattr(settings, prefixed(name), default))
