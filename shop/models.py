from django.db import models

class Company(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def products_count(self):
        return self.product_set.count()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    soni = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Sale(models.Model):
    Mijoz = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def sale_amount(self):
        return self.qty * self.product.price

    def save(self, *args, **kwargs):
        self.total_amount = self.sale_amount()

        product = self.product
        product.soni = product.soni - self.qty
        print(product.soni)
        product.save()

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Mijoz} - {self.product.title}"
