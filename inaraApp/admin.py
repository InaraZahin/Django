from django.contrib import admin

# Register your models here.
from .models import Home
admin.site.register(Home)

from .models import Hero, ContactU, Post, Message
admin.site.register(Hero)

admin.site.register(ContactU)

admin.site.register(Message)

from .models import Abt
admin.site.register(Abt)

from .models import Proc
admin.site.register(Proc)

from .models import Whyus
admin.site.register(Whyus)

from .models import Team
admin.site.register(Team)

from .models import Works
admin.site.register(Works)

from .models import Testi
# admin.site.register(Testi)

from .models import Blog
admin.site.register(Blog)
from .models import Callaction
admin.site.register(Callaction)

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',  'subject']


admin.site.register(Post, StatusAdmin)

class StatusAdmin1(admin.ModelAdmin):
    list_display = ['heading', 'details', 'review1',  'client1']


admin.site.register(Testi, StatusAdmin1)
