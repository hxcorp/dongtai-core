######################################################################
# @author      : bidaya0 (bidaya0@$HOSTNAME)
# @file        : res_header
# @created     : 星期三 1月 12, 2022 16:49:40 CST
#
# @description :
######################################################################


from django.db import models
from dongtai.utils.settings import get_managed
from dongtai.models.agent import IastAgent


class HeaderType(models.IntegerChoices):
    REQUEST = 1
    RESPONSE = 2


class ProjectSaasMethodPoolHeader(models.Model):
    key = models.CharField(max_length=255, blank=True, null=False)
    agent = models.ForeignKey(IastAgent,
                              models.DO_NOTHING,
                              blank=True,
                              null=True,
                              db_constraint=False)
    header_type = models.IntegerField(choices=HeaderType.choices,default=0)

    class Meta:
        managed = get_managed()
        db_table = 'iast_project_header'
