from django.db import models


from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    
    templates = "home/home_page.html" 

    max_count = 1

    sous_titre = models.CharField(max_length=100, blank=False, null=True)
    sous_style = RichTextField(features=["bold","italic"])
    sous_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    ) 

    sous_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel ("sous_titre"),
        FieldPanel ("sous_style"),
        ImageChooserPanel ("sous_image"),
        PageChooserPanel ("sous_page"),

    ]


