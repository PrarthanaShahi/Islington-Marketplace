from . models import SiteSetting
# Context processors are like magic helpers 
# that automatically add common, useful information to all your web pages, saving you time and keeping things consistent.
def site_settings(request):
    setting = SiteSetting.objects.first()
    return {'site_setting': setting}