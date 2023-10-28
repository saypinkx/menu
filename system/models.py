from django.db import models


# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)



#
# class ParentChild(models.Model):
#     parent = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
#     childes = models.ManyToManyField(Menu, blank=True,  related_name='childes')
