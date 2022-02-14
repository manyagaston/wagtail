
from wagtail.core import blocks

class TitreEtTextBlock (blocks.StructBlock):
    titre = blocks.CharBlock(required=True, help_text="titre d'article ")
    text = blocks.TextBlock(required=True, help_text="les contenues ")
    
    class Meta:
        templates = "streams/titre_et_text_block.html"
        icon = "edit"
        label = "Titre & Text"
    
class RichtextBlock(blocks.RichTextBlock):
    
    class Meta:
        templates = "streams/richtext-block.html"
        icon = "edit"
        label = "futll text"
        