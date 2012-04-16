from django import forms
from .widgets import AjaxFileWidget

class AjaxUploadForm(forms.Form):
    class Media:
        js = (
            #'ajaxuploader/js/jquery.js', # TODO: determine best way
            'ajaxuploader/js/fileuploader.js',
            )
        css = {'screen': ('ajaxuploader/css/fileuploader.css',)}

    file = forms.FileField(widget=AjaxFileWidget)

    def __init__(self, *args, **kwargs):
        try:
            self.request = kwargs.pop('request')
        except KeyError:
            raise RuntimeError(
                "AjaxUploadForm.__init__ requires a request object "
                "(for CSRF protection")
        super(AjaxUploadForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.set_request(self.request)
