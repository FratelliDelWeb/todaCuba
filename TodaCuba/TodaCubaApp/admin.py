from django.contrib import admin
from .models import QuienesSomos, QuienesSomosForm
from .models import Excursion1, Excursion1Form, Excursion2, Excursion2Form, Excursion3, Excursion3Form, Excursion4, Excursion4Form, Excursion5, Excursion5Form, Excursion6, Excursion6Form



from TodaCubaApp.models import SabiasQ
admin.site.register(SabiasQ)

from TodaCubaApp.models import Casas
admin.site.register(Casas)


from TodaCubaApp.models import Provincia
admin.site.register(Provincia)

class QuienesSomosAdmin(admin.ModelAdmin):
    form = QuienesSomosForm
admin.site.register(QuienesSomos, QuienesSomosAdmin)


class Excursion1Admin(admin.ModelAdmin):
    form = Excursion1Form
admin.site.register(Excursion1, Excursion1Admin)

class Excursion2Admin(admin.ModelAdmin):
    form = Excursion2Form
admin.site.register(Excursion2, Excursion2Admin)

class Excursion3Admin(admin.ModelAdmin):
    form = Excursion3Form
admin.site.register(Excursion3, Excursion3Admin)

class Excursion4Admin(admin.ModelAdmin):
    form = Excursion4Form
admin.site.register(Excursion4, Excursion4Admin)

class Excursion5Admin(admin.ModelAdmin):
    form = Excursion5Form
admin.site.register(Excursion5, Excursion5Admin)

class Excursion6Admin(admin.ModelAdmin):
    form = Excursion6Form
admin.site.register(Excursion6, Excursion6Admin)