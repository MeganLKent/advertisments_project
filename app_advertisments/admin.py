from django.contrib import admin
from .models import Advertisment # импортирую свою модель
# класс обьекта модели для подсказки
from django.db.models.query import QuerySet

# py manage.py createsuperuser - создания аккаунта супер пользователя
# пароль не отображается
# http://127.0.0.1:8000/admin



# класс для кастомизации модели в админке
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','auction', 'created_date', 'update_date'] # столбцы для отображения в таблице
    list_filter = ['auction', 'created_at', 'price']
    actions = ['make_action_as_false', 'make_action_as_true']
    fieldsets = (
        ('Общие', { # блок 1 
            "fields": (
                'title','description'    # поля блока
            ),
        }),
        ('Финансы', { # блок 2
            "fields": (
                'price','auction'    # поля блока
            ),
            'classes': ['collapse']
        })
    )
    


    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False) # обновить значение auction у выбранных записей на False


    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True) # обновить значение auction у выбранных записей на False








# подключение модели в админку и кастомной модели
admin.site.register(Advertisment, AdvertisementsAdmin)







# def dec(func):
#     def wrapper():
#         print()
#         func()
#         print()

#     return wrapper





# def add_list(some_list:list):
#     some_list.append()

# add_list()