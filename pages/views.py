from django.shortcuts import render

class HomePage(TemplateView): 
    template_name = "pages/index.html"
    
class AboutPage(TemplateView): 
    template_name = "pages/about.html"
    