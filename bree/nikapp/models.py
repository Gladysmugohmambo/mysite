""""from django.db import models
class series(models.model):
    artist=(models.CharField( '',MaxLength=300))
    series_title=(models.CharField('the originals',MaxLength=600)
    series_logo=(models.CharField(MaxLength=1000))
class season (models.model):
    series=models.ForeignKey(series,on_delete=models.CASCADE)
    file_type= models.CharField(MaxLength=30)
    season_title=models.CharField(MaxLength=250)"""



