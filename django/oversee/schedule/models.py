from django.db import models


class Availability(models.Model):
  id = models.AutoField(primary_key=True)
  times = models.CharField(max_length=200)

  def setTimes(self, x):
    self.times = json.dumps(x)

  def getTimes(self, x):
    return json.loads(self.times)

  def __str__(self):
    return str(self.times)

class User(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=60)
  availability = models.OneToOneField(Availability, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return "Name: " + str(self.name) + ", Availability: " + str(self.availability)

class Calendar(models.Model):
  name = models.CharField(max_length=20, default="My channel")

  def __str__(self):
    return str(self.name)


class Channel(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, default="My channel")
  users = models.ManyToManyField(User)
  calendar = models.OneToOneField(Calendar, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.name)
