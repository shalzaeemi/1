from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('يجب تحديد البريد الإلكتروني'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(_('البريد الإلكتروني'), unique=True)
    username = models.CharField(_('اسم المستخدم'), max_length=150, unique=True)
    first_name = models.CharField(_('الاسم الأول'), max_length=30)
    last_name = models.CharField(_('الاسم الأخير'), max_length=30)
    is_active = models.BooleanField(_('نشط'), default=True)
    date_joined = models.DateTimeField(_('تاريخ الانضمام'), auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('مستخدم')
        verbose_name_plural = _('المستخدمين')

    def __str__(self):
        return self.email
