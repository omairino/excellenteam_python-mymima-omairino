from django.contrib import admin

from facts.models import Fact,Song,Artist
admin.site.register(Fact)
admin.site.register(Song)
admin.site.register(Artist)
