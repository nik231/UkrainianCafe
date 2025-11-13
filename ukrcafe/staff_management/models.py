from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class StaffMember(models.Model):
    POSITION_CHOICES = [
        ('WAITER', _('Waiter')),
        ('CHEF', _('Chef')),
        ('MANAGER', _('Manager')),
        ('CASHIER', _('Cashier')),
    ]

    first_name = models.CharField(_('First Name'), max_length=50)
    last_name = models.CharField(_('Last Name'), max_length=50)
    position = models.CharField(_('Position'), max_length=20, choices=POSITION_CHOICES)
    hire_date = models.DateField(_('Hire Date'))
    phone_number = models.CharField(_('Phone Number'), max_length=15)
    email = models.EmailField(_('Email'), unique=True)
    is_active = models.BooleanField(_('Active'), default=True)
    hourly_wage = models.DecimalField(_('Hourly Wage'), max_digits=6, decimal_places=2,
                                      validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_position_display()}"

    class Meta:
        verbose_name = _('Staff Member')
        verbose_name_plural = _('Staff Members')
