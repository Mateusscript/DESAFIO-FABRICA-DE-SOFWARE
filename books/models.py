from uuid import uuid4
from django.db import models

class boocks(models.Model):
    id_book=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titler=models.CharField(max_length=300)
    autor=models.CharField(max_length=300)
    release_year=models.IntegerField(max_length=4)
    state=models.CharField(max_length=300)
    pages=models.IntegerField()
    publishing_company=models.CharField(max_length=300)
    create_at=models.DateField(auto_now_add=True)