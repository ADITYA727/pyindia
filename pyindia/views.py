from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /private/",
        "Sitemap: https://www.pyindia.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")