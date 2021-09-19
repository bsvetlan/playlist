from django.contrib import admin
import playlist_app.models as m

# Register your models here.
admin.site.register(m.Album)
admin.site.register(m.Executor)
admin.site.register(m.Playlist)
admin.site.register(m.Reward)
admin.site.register(m.Song)
admin.site.register(m.Songexecutor)
admin.site.register(m.Songplaylist)
admin.site.register(m.User)