from django.db import models
from rest_framework.exceptions import ValidationError

from common.models import CoreModel

#  TODO:
#   1. pageNumbers remove --> Done
#   2. Subtitle optional subsection --> Done
#   3. IsSubtitleActive basis par subtitle handle in Admin
#   4. Email validation on user via admin panel


class Literature(CoreModel):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50, help_text="Example: Edition of the literatures")
    is_subtitle_active = models.BooleanField(help_text="To keep subtitle visible on app screen")
    is_sequence_active = models.BooleanField(help_text="To keep sequence visible on app screen")

    class Meta:
        db_table = 'literature'

    def __str__(self):
        return self.title


class LiteratureSubSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50, blank=True)
    main_content = models.TextField()
    literature = models.ForeignKey(Literature, related_name="literature", on_delete=models.CASCADE)

    class Meta:
        db_table = 'literature_sub_section'

    def __str__(self):
        return self.title
