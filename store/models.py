import random
import string
from django.db import models
from account.models import Account, Customer
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


def upload_location(instance, filename):
    file_path = 'store/{owner_id}/{store}-{filename}'.format(
                owner_id=str(instance.store.owner.id),store=str(instance.store), filename=filename)
    return file_path


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def _str_(self):
        return self.title


class Store(models.Model):
    store_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.TextField(max_length=5000, null=False, blank=False)
    slug = models.SlugField(blank=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

def pre_save_store_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(rand_slug() + "-" + instance.store_name)

pre_save.connect(pre_save_store_receiver, sender=Store)


class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=5000, null=False, blank=False)
    mrp = models.IntegerField()
    sale_price = models.IntegerField()
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


# class Order(models.Model):
#     ordered_at = models.DateTimeField(auto_now_add=True)
#     product = models.ManyToManyField(Product)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)