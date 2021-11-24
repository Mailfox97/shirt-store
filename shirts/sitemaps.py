from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'contact', 'orders', 'products', 'checkout', 'cart_detail', 'profile']
    def location(self, item):
        return reverse(item)