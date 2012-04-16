import datetime
from io import FileIO, BufferedWriter
import os

from django.conf import settings
from django.utils.encoding import force_unicode, smart_str

from .. import settings as ajaxuploader_settings
from .base import AbstractUploadBackend

class LocalUploadBackend(AbstractUploadBackend):
    UPLOAD_DIR = ajaxuploader_settings.UPLOAD_DIRECTORY
    # TODO: allow this to be overridden per-widget/view

    def setup(self, filename):
        self._relative_path = os.path.normpath(
            os.path.join(
                force_unicode(
                    datetime.datetime.now().strftime( # allow %Y, %s, etc
                        smart_str(self.UPLOAD_DIR))),
                filename))
        self._path = os.path.join(settings.MEDIA_ROOT, self._relative_path)
        try:
            os.makedirs(os.path.realpath(os.path.dirname(self._path)))
        except:
            pass
        self._dest = BufferedWriter(FileIO(self._path, "w"))

    def upload_chunk(self, chunk):
        self._dest.write(chunk)

    def upload_complete(self, request, filename):
        self._dest.close()
        return {"path": self._relative_path}

    def update_filename(self, request, filename):
        return ajaxuploader_settings.SANITIZE_FILENAME(filename)
