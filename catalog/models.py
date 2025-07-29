from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class PartnerOfferPage(Page):
    description = RichTextField(blank=True)
    link = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('link'),
    ]
