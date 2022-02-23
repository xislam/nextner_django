import datetime

from django.core.files import File
from django.test import TestCase

from delivery.models import *
import mock


class TestAppModels(TestCase):

    def test_model_str(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        product_type_name = ProductType.objects.create(name="Экспорт")
        delivery_test = Delivery.objects.create(product_name='Машина',
                                                delivery_date=datetime.datetime.now().date(), file=file_mock)
        delivery_test.product_type.set([product_type_name.pk])
        multiple_addresses = MultipleAddresses.objects.create(delivery=delivery_test, address='тест')
        self.assertEqual(str(product_type_name), "Экспорт")
        self.assertEqual(str(delivery_test), 'Машина')
        self.assertEqual(str(multiple_addresses), 'Машина')
