from django.db import models


class OperatingSystem(models.Model):

    """
    OperatingSystem Model
    Contains list of operating systems
    """

    name = models.CharField(max_length=50)
    version = models.FloatField()

    def __str__(self):
        return self.name+" "+str(self.version)


class Server(models.Model):

    """
    Server Model
    Contains list of servers
    """

    TYPE_OF_SERVER = (
        ('DNS', 'DNS'),
        ('WEB', 'WEB'),
        ('DB', 'DB'),
        ('APP', 'APP'),
    )

    hostname = models.CharField(max_length=30)
    ipv4 = models.CharField(max_length=15)
    ipv6 = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    enabled = models.BooleanField(default=True)
    os = models.ForeignKey('OperatingSystem', on_delete=models.CASCADE)
    types = models.CharField(max_length=15, choices=TYPE_OF_SERVER)
    created= models.DateField(auto_now_add=True)
