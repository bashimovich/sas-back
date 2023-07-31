from rest_framework import serializers
from sas.models import *

class ImageSerializer(serializers.ModelSerializer):
    src = serializers.ImageField()

    class Meta:
        model = Image
        fields = ("src", ) 

class MobileImageSerializer(serializers.ModelSerializer):
    src = serializers.ImageField()

    class Meta:
        model = Image
        fields = ("src", ) 

class LogoSerializer(serializers.ModelSerializer):
    src = serializers.ImageField()

    class Meta:
        model = Logo
        fields = ("src", ) 

class SubInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoSub
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    subinfos = SubInfoSerializer(many=True)

    class Meta:
        model = Info
        fields = '__all__'

class SiteLogoSerializer(serializers.ModelSerializer):
    logo = LogoSerializer(many=True)

    class Meta:
        model = SiteLogo
        fields = "__all__"

class NavBarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NavBar
        fields = "__all__"

class SliderSerializer(serializers.ModelSerializer):
    images_for_web = ImageSerializer(many=True)
    images_for_mobile = ImageSerializer(many=True)

    class Meta:
        model = Slider
        fields = "__all__"

class MarketSerializer(serializers.ModelSerializer):
    images_for_web = ImageSerializer(many=True)
    images_for_mobile = ImageSerializer(many=True)

    class Meta:
        model = Market
        fields = "__all__"

class OnlineMarketSerializer(serializers.ModelSerializer):
    images_for_web = ImageSerializer(many=True)
    images_for_mobile = ImageSerializer(many=True)

    class Meta:
        model = OnlineMarket
        fields = "__all__"

class CoffeShopSerialzer(serializers.ModelSerializer):
    images_for_web = ImageSerializer(many=True)
    images_for_mobile = ImageSerializer(many=True)

    class Meta:
        model = CoffeShop
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    images_for_web = ImageSerializer(many=True)
    images_for_mobile = ImageSerializer(many=True)

    class Meta:
        model = Banner
        fields = "__all__"

class PartnershipSerializer(serializers.ModelSerializer):
    logo = LogoSerializer(many=True)

    class Meta:
        model = Partnership
        fields = "__all__"