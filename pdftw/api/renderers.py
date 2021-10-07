import pdfkit
from django.utils.translation.trans_null import gettext_noop as _noop
from rest_framework.renderers import TemplateHTMLRenderer


class TemplatePDFRenderer(TemplateHTMLRenderer):
    media_type = 'application/pdf'
    format = 'pdf'
    charset = None
    render_style = "binary"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        out = super().render(data, accepted_media_type, renderer_context)
        return pdfkit.from_string(
            out,
            False,
            options={
                'page-size': _noop('A4'),
                'encoding': _noop('UTF-8'),
                'margin-top': _noop('0.5in'),
                'margin-right': _noop('0.75in'),
                'margin-bottom': _noop('0.5in'),
                'margin-left': _noop('0in'),
                'quiet': _noop(''),
                'orientation': _noop('portrait'),
            },
        )
