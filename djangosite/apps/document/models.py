from django.db import models
from django.utils.translation import ugettext_lazy as _


class Document(models.Model):
    '這裡代表每一次的驗證, 及驗證時相關的資料'
    task = models.ForeignKey('project.Task',
                                   on_delete=models.CASCADE,
                                   related_name='document_task',
    )
    inspector = models.CharField(max_length=20, blank=True)


class DocumentItem(models.Model):
    document = models.ForeignKey('Document',
                                    on_delete=models.CASCADE,
                                    related_name='item',
    )
    name = models.CharField(_("Name"), max_length=30, blank=True)


    doc = models.FileField(_("document"), blank=True)
    image = models.ImageField(_("image"), blank=True)
    
    class Result(models.TextChoices):
        PASS = 'PASS'
        FAIL = 'FAIL'
        EMPTY = 'EMPTY'

    check_result = models.CharField(
        max_length=5,
        choices=Result.choices,
        default=Result.EMPTY,
    )
    def __str__(self):
        return self.name