from django.contrib.sitemaps import Sitemap
from shirts.models import Tshirt

class TshirtSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    # def items(self):
    #     return Tshirt.objects.all()
