from django.contrib import admin

from .models import *

admin.site.register(Users)
admin.site.register(Notifications)
admin.site.register(Sports)
admin.site.register(Teams)
admin.site.register(Playgrounds)
admin.site.register(Events)
admin.site.register(NotificationsOfUsers)
admin.site.register(SportsOfPlaygrounds)
admin.site.register(SportsOfUsers)
admin.site.register(TeamsOfUsers)
admin.site.register(SocialNetworksOfUsers)