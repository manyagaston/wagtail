from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks

# Create your models here.

class BlogPage(Page):

    templates = "blog/blog_page.html"
    
    blog_titre = models.CharField(max_length=100, null=True, blank=True)
    
    content = StreamField([
        ("titre_et_text_block", blocks.TitreEtTextBlock()),
        ("richtext_block", blocks.RichtextBlock()),
        ],
        null = True,
        blank = True,
        )
    
    content_panels = Page.content_panels + [
        FieldPanel("blog_titre"),
        StreamFieldPanel("content"),
    ]
    
    class Meta:
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"
