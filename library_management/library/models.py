from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    review = models.IntegerField()
    start_time = models.DateTimeField(auto_now_add=True)
    finish = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    # class Meta:
    #     order = ['finish']
