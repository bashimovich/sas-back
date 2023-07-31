from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from sas.models import *
from sas.api.serializers import *
from rest_framework.viewsets import ReadOnlyModelViewSet

@api_view(["POST"])
def contact_us_send_mail(request):
    if request.method == "POST":
        from_email = request.data.get('email')
        message = request.data.get('message')
        name = request.data.get('name')
        to_email = settings.TO_EMAIL

        # mail sending script hehe
        SEND_MAIL = True 
    
        if SEND_MAIL:
            ContactUsSendMail.objects.create(
                from_email = from_email,
                to_email = to_email, 
                name = name,
                message=message,
            )
            return Response({'data':'Succesfully sent Mail'}, status=status.HTTP_201_CREATED)
        return Response({'data':'Could Not send Mail'}, status=status.HTTP_201_CREATED)


class InfoViewSet(ReadOnlyModelViewSet):
    queryset = Info.objects.filter(is_active=True)
    serializer_class = InfoSerializer

class SiteLogoViewSet(ReadOnlyModelViewSet):
    queryset = SiteLogo.objects.filter(is_active=True)
    serializer_class = SiteLogoSerializer

class NavBarViewSet(ReadOnlyModelViewSet):
    queryset = NavBar.objects.filter(is_active=True)
    serializer_class = NavBarSerializer

class SliderViewSet(ReadOnlyModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer

class MarketViewSet(ReadOnlyModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = Market

class OnlineMarketViewSet(ReadOnlyModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = OnlineMarketSerializer

class CoffeShopViewSet(ReadOnlyModelViewSet):
    queryset = Slider.objects.filter(is_active=True)
    serializer_class = CoffeShopSerialzer

class BannerViewSet(ReadOnlyModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer

class PartnershipViewSet(ReadOnlyModelViewSet):
    queryset = Partnership.objects.filter(is_active=True).order_by('-id')
    serializer_class = PartnershipSerializer