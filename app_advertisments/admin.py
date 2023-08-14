from django.contrib import admin
from .models import Advertisment # импортирую свою модель
# класс обьекта модели для подсказки
from django.db.models.query import QuerySet
from django.utils.safestring import mark_safe 

# py manage.py createsuperuser - создания аккаунта супер пользователя
# пароль не отображается
# http://127.0.0.1:8000/admin



# класс для кастомизации модели в админке
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title','description','price', 'created_date', 'update_date', 'auction', 'get_html_image'] # столбцы для отображения в таблице
    list_filter = ['auction', 'created_at', 'price']
    actions = ['make_action_as_false', 'make_action_as_true']
    fieldsets = (
        ('Общие', { # блок 1 
            "fields": (
                'title','description', 'user', 'image'   # поля блока
            ),
        }),
        ('Финансы', { # блок 2
            "fields": (
                'price','auction'    # поля блока
            ),
            'classes': ['collapse']
        })
    )
    
    def get_html_image (self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")
    
    get_html_image.short_description = 'мини-изображение'
    
    
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