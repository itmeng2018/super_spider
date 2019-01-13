from django.db import models
from django.contrib.auth.models import AbstractUser
from db_tools.base_model import BaseModel


class User(AbstractUser, BaseModel):
    """用户模型类"""

    phone = models.CharField(max_length=11, verbose_name='手机号', default=None)
    permission_level = models.IntegerField(default=0, verbose_name='权限等级')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
