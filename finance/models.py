from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class FinancePage(Page):
    body = RichTextField()
    content_panels = Page.content_panels + [FieldPanel('body')]
