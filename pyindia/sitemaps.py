from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'services', 'blog', 'detail', 'team', 'testimonial']  # Add your URL names here

    def location(self, item):
        return reverse(item)
    
    def lastmod(self, item):
        return None  # Modify this if you have a last modified date for each item
