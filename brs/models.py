from django.db import models

# Create your models here.
class start(models.Model):
    from_s=models.CharField(max_length=20)

    def __str__(self):
        return self.from_s
    
class stop(models.Model):
    to_s=models.CharField(max_length=20)

    def __str__(self):
        return self.to_s
    
class bus(models.Model):
    bus_name=models.CharField(max_length=20)
    from_s=models.ForeignKey(start,on_delete=models.CASCADE)
    to_s=models.ForeignKey(stop,on_delete=models.CASCADE)

    def __str__(self):
        return self.bus_name
    
class bookings(models.Model):
    name=models.CharField(max_length=20)  
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    from_s=models.ForeignKey(start,on_delete=models.CASCADE)
    to_s=models.ForeignKey(stop,on_delete=models.CASCADE)
    bus_name=models.ForeignKey(bus,on_delete=models.CASCADE)
    date=models.DateField()
