from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSiteSetting):
    instagram = models.URLField(max_length=100, blank=True)

    panels = [
        FieldPanel("instagram")
    ]