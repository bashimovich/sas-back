from django.db import models
from django.utils.html import mark_safe
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField

# Create your models here.

class Image(models.Model):
    src = models.ImageField(upload_to="images")
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def img_preview(self):
        return mark_safe(f'<img src="{self.src.url}" width=70 height=70>')

class MobileImage(models.Model):
    src = models.ImageField(upload_to="mobile-images")
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def img_preview(self):
        return mark_safe(f'<img src="{self.src.url}" width=70 height=70>')

class Logo(models.Model):
    src = models.ImageField(upload_to="logo")
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def img_preview(self):
        return mark_safe(f'<img src="{self.src.url}" width=70 height=70>')

class ContactUsSendMail(models.Model):
    from_email = models.EmailField()
    to_email = models.EmailField()
    name = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.from_email

    class Meta:
        verbose_name_plural = "Contact Messages"
    
class InfoSub(models.Model):
    data = models.CharField(max_length=200, blank=False, null=False)
    icon = RichTextField(null=True)
    info = models.ForeignKey('Info', related_name='subinfos', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Company Informations"

    def __str__(self):
        return self.data

class Info(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Company Informations Collection"

    def __str__(self):
        return self.name

class SiteLogo(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    logo = GenericRelation('Logo', blank=False, null=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Company Logo"

    def __str__(self):
        return self.name


class NavBar(models.Model):
    NAVBAR_POSITION = [
        ('header', "Header"),
        ('footer', "Footer"),
        ('header_footer', "Twice"),
    ]
    name = models.CharField(max_length=200, blank=False, null=False)
    link = models.CharField(max_length=200, blank=False, null=False)
    _type = models.CharField(max_length=30, choices=NAVBAR_POSITION, default='header')

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "NavBar List"

    def __str__(self):
        return self.name

class Slider(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = RichTextField(null=True)
    button = models.CharField(max_length=200, blank=False, null=False)
    button_link = models.CharField(max_length=200, blank=False, null=False)
    images_for_web = GenericRelation('Image', blank=False, null=False)
    images_for_mobile = GenericRelation('Image', blank=False, null=False)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Slider List"

    def __str__(self):
        return self.title

class Market(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = RichTextField(null=True)
    address = models.CharField(max_length=200, blank=False, null=False)
    icon = RichTextField(null=True)
    images_for_web = GenericRelation('Image', blank=False, null=False)
    images_for_mobile = GenericRelation('Image', blank=False, null=False)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Market Section"

    def __str__(self):
        return self.title

class OnlineMarket(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = RichTextField(null=True)
    button = models.CharField(max_length=200, blank=False, null=False)
    button_link = models.CharField(max_length=200, blank=False, null=False)
    images_for_web = GenericRelation('Image', blank=False, null=False)
    images_for_mobile = GenericRelation('Image', blank=False, null=False)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Online Market"

    def __str__(self):
        return self.title


class CoffeShopList(models.Model):
    data = models.CharField(max_length=200, blank=False, null=False)
    icon = RichTextField(null=True)
    coffeshop = models.ForeignKey('CoffeShop', related_name='coffeshoplists', on_delete=models.CASCADE, default=1)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Coffe Shop Lists"

    def __str__(self):
        return self.data

class CoffeShop(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = RichTextField(null=True)
    button = models.CharField(max_length=200, blank=False, null=False)
    button_link = models.CharField(max_length=200, blank=False, null=False)
    icon = RichTextField(null=True)
    images_for_web = GenericRelation('Image', blank=False, null=False)
    images_for_mobile = GenericRelation('Image', blank=False, null=False)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Coffe Shop"

    def __str__(self):
        return self.title

class Banner(models.Model):
    images_for_web = GenericRelation('Image', blank=False, null=False)
    images_for_mobile = GenericRelation('Image', blank=False, null=False)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Banner"

    def __str__(self):
        return "Banner ID: " + str(self.id)

class Partnership(models.Model):   
    logo = GenericRelation('Logo', blank=False, null=False)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Partnership"