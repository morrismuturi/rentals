from django.db import models

# Create your models here.
class RoomType(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    
    def __str__(self):
        return self.name

class Purpose(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    county=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    
    def __str__(self):
        return self.county
    
class Room(models.Model):
    room_type_id=models.ForeignKey(RoomType,on_delete=models.CASCADE)
    purpose_id=models.ForeignKey(Purpose,on_delete=models.CASCADE)
    location_id=models.ForeignKey(Location,on_delete=models.CASCADE)
    floor=models.TextField()
    position_on_main_building=models.IntegerField()
    parking_facility_adjacency=models.BooleanField()
    
    
    
