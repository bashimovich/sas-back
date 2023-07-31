from django.urls import path, include
from rest_framework import routers
from sas.api.views import contact_us_send_mail
from . import views as api_viewset

router = routers.DefaultRouter()
router.register(r'company-information', api_viewset.InfoViewSet, basename="company-information")
router.register(r'site-logo', api_viewset.SiteLogoViewSet, basename="site-logo")
router.register(r'navbar', api_viewset.NavBarViewSet, basename="navbar")
router.register(r'slider', api_viewset.SliderViewSet, basename="slider")
router.register(r'market', api_viewset.MarketViewSet, basename="market")
router.register(r'online-market', api_viewset.OnlineMarketViewSet, basename="online-market")
router.register(r'coffe-shop', api_viewset.CoffeShopViewSet, basename="coffe-shop")
# router.register(r'statistics', api_viewset.StatisticsViewSet, basename="statistics")
# router.register(r'video-section', api_viewset.VideoSectionViewSet,
#                 basename="video-section")
# router.register(r'image-section', api_viewset.ImageSectionViewSet, basename="image-section")
# router.register(r'products', api_viewset.ProductsViewSet, basename="products")
router.register(r'banner', api_viewset.BannerViewSet, basename="banner")
# router.register(r'certificates', api_viewset.CertificatesViewSet,
#                 basename="certificates")
# router.register(r'news', api_viewset.NewsViewSet, basename="news")
# router.register(r'gallery', api_viewset.GalleryViewSet, basename="gallery")
# router.register(r'contact-us', api_viewset.ContactUsViewSet, basename="contact-us")
router.register(r'partnership', api_viewset.PartnershipViewSet, basename="partnership")

urlpatterns = [
    path('send-mail/', contact_us_send_mail, name='send-mail'),
    path(r'', include(router.urls)),
]
