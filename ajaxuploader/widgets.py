from django.forms.widgets import FileInput
from django.middleware.csrf import get_token
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class AjaxFileWidget(FileInput):
    request = None

    def set_request(self, request):
        self.request = request

    def render(self, name, value, attrs=None):
        return mark_safe(
            render_to_string(
                'ajaxuploader/widget.html',
                {'csrf_token': get_token(self.request)}))
