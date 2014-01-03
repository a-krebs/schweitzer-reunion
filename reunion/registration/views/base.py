from django.views.generic.base import TemplateView


class BaseApplicationView(TemplateView):
    """
    Main entry point for the javascript application.
    """
    template_name = 'registration/main.haml'