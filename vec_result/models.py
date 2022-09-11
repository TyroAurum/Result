from django.db import models

# Create your models here.


class PinkIT(models.Model):
    Register_No = models.BigIntegerField(
        blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=3, blank=False, null=True)
    P21CH101T = models.CharField(max_length=3, blank=False, null=True)
    P21EN101T = models.CharField(max_length=3, blank=False, null=True)
    P21ME101T = models.CharField(max_length=3, blank=False, null=True)
    P21CS101T = models.CharField(max_length=3, blank=False, null=True)
    P21CH102L = models.CharField(max_length=3, blank=False, null=True)
    P21CS102L = models.CharField(max_length=3, blank=False, null=True)
    P21EN102L = models.CharField(max_length=3, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        db_table = 'PinkIT'

    def __str__(self):
        return self.Name
