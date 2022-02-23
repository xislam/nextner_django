from django.db import models


class ProductType(models.Model):
    """Тип продукта"""
    name = models.CharField(verbose_name="Наименование типа", max_length=125)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    """Данные товара для доставки"""
    product_name = models.CharField(verbose_name='Имя товара', max_length=125)
    product_type = models.ManyToManyField(ProductType, verbose_name="Тип товака")
    delivery_date = models.DateField(verbose_name='Дата доставки')
    file = models.FileField(verbose_name="Файл", upload_to="delivery")

    def __str__(self):
        return self.product_name


class MultipleAddresses(models.Model):
    """Множественных адресов пунктов выдачи"""
    delivery = models.ForeignKey(Delivery, verbose_name='Множественных Адресов Указанных Выдачи',
                                 on_delete=models.CASCADE)
    address = models.TextField(verbose_name="Наимнование адриса")

    def __str__(self):
        return self.delivery.product_name


