from django.contrib import admin
from sas.models import *
from django.utils.html import format_html, mark_safe, format_html_join
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

# Register your models here.


class ImageInline(GenericStackedInline):
    model = Image

class MobileImageInline(GenericStackedInline):
    model = MobileImage

class LogoInline(GenericStackedInline):
    model = Logo

class ContactUsSendMailAdmin(admin.ModelAdmin):
    list_display = ("from_email", "created_at", )
    readonly_fields = ("from_email", "to_email", "name", "message", "created_at", )


class InfoSubAdmin(admin.ModelAdmin):
    list_display = ("data",)

class InfoAdmin(admin.ModelAdmin):
    list_display = ("name",)

class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ("get_logos", "name", "is_active", "updated_at",)
    list_editable = ("is_active",)
    list_display_links = ("get_logos", "name",)
    inlines = (LogoInline,)

    def get_logos(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.logo.all()))
    get_logos.short_description = "Site Logo"

class NavBarAdmin(admin.ModelAdmin):
    list_display = ("name", "_type", "is_active", "updated_at",)
    list_editable = ("is_active",)

class SliderAdmin(admin.ModelAdmin):
    list_display = ("get_images_web","get_images_mobile", "title", "is_active", "updated_at",)
    list_editable = ("is_active",)
    inlines = (ImageInline, MobileImageInline, )

    def get_images_web(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_web.all()))
    def get_images_mobile(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_mobile.all()))
    get_images_web.short_description = "Slider Web Image"
    get_images_mobile.short_description = "Slider Mobile Image"

class MarketAdmin(admin.ModelAdmin):
    list_display = ("get_images_web","get_images_mobile", "title", "is_active", "updated_at",)
    list_editable = ("is_active",)
    inlines = (ImageInline, MobileImageInline, )

    def get_images_web(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_web.all()))
    def get_images_mobile(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_mobile.all()))
    get_images_web.short_description = "Web Image"
    get_images_mobile.short_description = "Mobile Image"

class OnlineMarketAdmin(admin.ModelAdmin):
    list_display = ("get_images_web","get_images_mobile", "title", "is_active", "updated_at",)
    list_editable = ("is_active",)
    inlines = (ImageInline, MobileImageInline, )

    def get_images_web(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_web.all()))
    def get_images_mobile(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_mobile.all()))
    get_images_web.short_description = "Web Image"
    get_images_mobile.short_description = "Mobile Image"


class CoffeShopAdmin(admin.ModelAdmin):
    list_display = ("get_images_web","get_images_mobile", "title", "is_active", "updated_at",)
    list_editable = ("is_active",)
    inlines = (ImageInline, MobileImageInline, )

    def get_images_web(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_web.all()))
    def get_images_mobile(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_mobile.all()))
    get_images_web.short_description = "Web Image"
    get_images_mobile.short_description = "Mobile Image"

class CoffeShopListAdmin(admin.ModelAdmin):
    list_display = ("get_icon", "data",)

    def get_icon(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.icon.all()))

    get_icon.short_description = "Coffe Shop List"


class BannerAdmin(admin.ModelAdmin):
    list_display = ("get_images_web", "get_images_mobile", "is_active", "updated_at",)
    list_editable = ("is_active",)
    inlines = (ImageInline, MobileImageInline)

    def get_images_web(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_web.all()))
    def get_images_mobile(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images_for_mobile.all()))
    get_images_web.short_description = "Web Image"
    get_images_mobile.short_description = "Mobile Image"


class PartnershipAdmin(admin.ModelAdmin):
    list_display = ("get_logo",  "is_active", "updated_at",)
    list_editable = ("is_active",)
    inlines = (LogoInline, )

    def get_logo(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.logo.all()))
    get_logo.short_description = "Parter's Logo"

admin.site.register(ContactUsSendMail, ContactUsSendMailAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(InfoSub, InfoSubAdmin)
admin.site.register(SiteLogo, SiteLogoAdmin)
admin.site.register(NavBar, NavBarAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(OnlineMarket, OnlineMarketAdmin)
admin.site.register(CoffeShop, CoffeShopAdmin)
admin.site.register(CoffeShopList, CoffeShopListAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Partnership, PartnershipAdmin)