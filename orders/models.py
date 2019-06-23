from django.db import models

# Create your models here.
class Pizza(models.Model):
    size = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    num_toppings = models.IntegerField()
    speical = models.BooleanField(default=False)

    def __str__(self):
        if self.num_toppings == 0 and self.speical == True:
            return f"speial pizza"
        elif self.num_toppings == 0 and self.speical == False:
            return f"{self.size} {self.kind} pizza with cheese"
        else:
            return f"{self.size} {self.kind} pizza with {self.num_toppings} toppings"

class PizzaPrice(models.Model):
    kind = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="prices")
    price = models.FloatField()

    def __str__(self):
        return f"{self.kind} costs ${self.price}"

class PizzaTopping(models.Model):
    kind = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.kind}"

class Salads(models.Model):
    kind = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.kind} costs ${self.price}"

class DinnerPlatters(models.Model):
    kind = models.CharField(max_length=64)
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size} {self.kind}"

class DinnerPlattersPrice(models.Model):
    kind = models.ForeignKey(DinnerPlatters, on_delete=models.CASCADE, related_name="DPPrices")
    price = models.FloatField()

    def __str__(self):
        return f"{self.kind} costs ${self.price}"

class Pasta(models.Model):
    kind = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.kind} costs ${self.price}"


class Subs(models.Model):
    size = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    extracheese = models.BooleanField(default=False)
    def __str__(self):
        if self.extracheese == True:
            return f"{self.size} {self.kind} with extra cheese"
        else:
            return f"{self.size} {self.kind}"

class SubsPrice(models.Model):
    kind = models.ForeignKey(Subs, on_delete=models.CASCADE, related_name="SubsPrices")
    price = models.FloatField()

    def __str__(self):
        return f"{self.kind} costs ${self.price}"

class SubsSteak(models.Model):
    size = models.CharField(max_length=64)
    addonkind = models.CharField(max_length=64)
    extracheese = models.BooleanField(default=False)
    def __str__(self):
        if self.extracheese == True:
            return f"{self.size} steak with {self.addonkind} and extra cheese"
        else:
            return f"{self.size} steak with {self.addonkind}"

class SubsSteakPrice(models.Model):
    kind = models.ForeignKey(SubsSteak, on_delete=models.CASCADE, related_name="ssPrices")
    price = models.FloatField()

    def __str__(self):
        return f"{self.kind} costs ${self.price}"

class Order(models.Model):
    user = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    price = models.FloatField()
    toppings = models.CharField(max_length=64)
    status = models.CharField(default="pending", max_length=64)
    def __str__(self):
        if self.toppings!="0" and self.toppings!="":
            return f"{self.user} costs ${self.price} to buy {self.product} with {self.toppings}: {self.status}"
        else:
            return f"{self.user} costs ${self.price} to buy {self.product}: {self.status}"
