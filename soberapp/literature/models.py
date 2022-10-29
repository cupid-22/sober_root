from django.db import models
from common.models import CoreModel


class Literature(CoreModel):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=50, help_text="Example: Edition of the literatures")

    class Meta:
        db_table = 'literature'

    def __str__(self):
        return self.title


class LiteratureSubSection(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=50)
    is_sub_title_active = models.BooleanField(default=True)
    main_content = models.TextField()
    literature = models.ForeignKey(Literature, related_name="literature", on_delete=models.CASCADE)

    class Meta:
        db_table = 'literature_sub_section'

    def __str__(self):
        return self.title
