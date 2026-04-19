from django.db import models

# Create your models here.
class Personnel(models.Model):
  full_name = models.CharField(max_length=150)
  rank_position= models.CharField(max_length=100)
  unit_section= models.CharField(max_length=100)
  contact_number= models.CharField(max_length=20, blank=True,null=True)

  def __str__(self):
    return self.full_name
