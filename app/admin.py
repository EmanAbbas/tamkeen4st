from django.contrib import admin
from .models import Project ,Sponsor,ContactMessage
from app.models import Subscriber



admin.site.register(Sponsor)
admin.site.register(Subscriber)
admin.site.register(Project)
admin.site.register(ContactMessage)










admin.site.site_title='Tamkeen4st Adminstration'
admin.site.index_title='Tamkeen4st Adminstration'
admin.site.site_header='Tamkeen4st Adminstration'


