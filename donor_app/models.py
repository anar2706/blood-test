from django.db import models
from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField
from region_app.models import *
from django.utils.translation import ugettext_lazy as _

class Donor(models.Model):
    BGROUP_1_P = 1
    BGROUP_1_M = 2
    BGROUP_2_P = 3
    BGROUP_2_M = 4
    BGROUP_3_P = 5
    BGROUP_3_M = 6
    BGROUP_4_P = 7
    BGROUP_4_M = 8

    GENDER_MALE = 1
    GENDER_FEMALE = 2

    bgroup_choices = {
        BGROUP_1_P: _('+A'),
        BGROUP_1_M: _('-A'),
        BGROUP_2_P: _('+B'),
        BGROUP_2_M: _('-B'),
        BGROUP_3_P: _('+O'),
        BGROUP_3_M: _('-O'),
        BGROUP_4_P: _('+AB'),
        BGROUP_4_M: _('-AB'),
    }

    gender_choices = {
        GENDER_MALE: _('Male'),
        GENDER_FEMALE: _('Female')
    }


    # photo = models.ImageField(_("Photo"), blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=120)
    last_name = models.CharField(_("Last Name"), max_length=120)
    phone = models.CharField(max_length=255)
    gender = models.IntegerField(_("Gender"), choices=tuple(gender_choices.items()))
    blood_group = models.IntegerField(_("Blood group"), choices=tuple(bgroup_choices.items()))
    height = models.IntegerField(_("Height"), blank=True, null=True)
    county = models.ForeignKey(County, verbose_name=_("County"), on_delete=models.DO_NOTHING)
    is_private = models.BooleanField(_("Account is private"), default=False)
    is_closed = models.BooleanField(_("Close account"), default=False)
    is_contact_private = models.BooleanField(_("Contact is private"), default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.bgroup_choices[self.blood_group]}"


    class Meta:
        verbose_name = 'Donor'
        verbose_name_plural = 'Donors'
        index_together = ['first_name', 'last_name', 'phone', 'is_private', 'is_closed']