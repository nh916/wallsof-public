from django.contrib import admin
from wallOf.models import *

admin.site.site_header = 'thewallsof.com'

admin.site.register(ModelPosts)
admin.site.register(Modelsecrets)
admin.site.register(ModelAdvice)
admin.site.register(ModelJoy)
admin.site.register(ModelSpam)
admin.site.register(ModelGraduation)