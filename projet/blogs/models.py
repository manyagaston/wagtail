from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel

    

# Create your models here.
class BlogsPage(Page):
    
    templates = "blogs/blogs_page.html" 
    
    titre = RichTextField(blank=True)
    sous_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    ) 
   
    content_panels = Page.content_panels + [
        FieldPanel("titre",classname="full"),
        ImageChooserPanel ("sous_image"),
       
    ]
    
    subpage_types = ["PostPage"]
    
class PostPage(Page):
    
    templates = "blogs/post_page.html" 
    
    date = models.DateField("Post Date")
    memoire = models.CharField(max_length=500)
    body = RichTextField()
    sous_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    ) 

    
    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("memoire"),
        FieldPanel("body",classname="full"),
        ImageChooserPanel ("sous_image"),
        
    ]
    
    parent_page_types = ["BlogsPage"]
