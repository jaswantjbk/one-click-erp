from .models import Module

def enabled_modules(request):
    return {
        'modules': Module.objects.filter(is_enabled=True)
    }
