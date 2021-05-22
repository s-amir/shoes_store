from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="نام")
    last_name = models.CharField(max_length=30, verbose_name="نام خانوادگی")
    address = models.TextField(max_length=200, verbose_name="آدرس ")
    postal_code = models.IntegerField( verbose_name='کد پستی', null=True)
    phone_number = models.CharField(max_length=11, verbose_name='شماره همراه')

    def __str__(self):
        return str(self.id)


class Employee(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="نام")
    last_name = models.CharField(max_length=30, verbose_name="نام خانوادگی")

    def __str__(self):
        return str(self.id)


class Company(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام شرکت سازنده")

    def __str__(self):
        return self.name + str(self.id)


class Shoes(models.Model):
    STATUS_CHOICE = (
        ('available', 'Available'),
        ('out_of_stock', 'Out of stock'),
    )
    name = models.CharField(max_length=30, verbose_name="نام")
    color = models.CharField(max_length=8, verbose_name='رنگ')
    size = models.CharField(max_length=2, verbose_name='سایز')
    number = models.IntegerField(verbose_name='تعداد')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Out of stock')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=12, verbose_name="قیمت")

    def __str__(self):
        return self.name


class OrderRecord(models.Model):
    customer_id = models.OneToOneField('shoes_shop.Customer', on_delete=models.SET_NULL, null=True)
    employee_id = models.OneToOneField('shoes_shop.Employee', on_delete=models.SET_NULL, null=True)
    shoe_id = models.OneToOneField('shoes_shop.Shoes', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(verbose_name='تعداد')

    # def save(self, **kwargs):
    #     ordered_shoes = Shoes.objects.get(id=self.shoe_id)
    #     if int(ordered_shoes.number) > 0:
    #         ordered_shoes.number -= 1
    #         # ordered_shoes.save()
    #         # super(OrderRecord, self).save()
    #     else:
    #         return -1

    def __str__(self):
        return f"{self.customer_id} --- {self.employee_id}"
