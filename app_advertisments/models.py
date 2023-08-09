from django.db import models

        # модули для настройки методов админки
from django.contrib import admin
from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html
        #

# Create your models here.
# тестовый класс
'''class Cats(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)'''


# главный

# venv/Scripts/activate   
# py manage.py makemigrations
# py manage.py migrate
# заголовок - описание - цена - дата создания - дата обновления - тогр



class Advertisment(models.Model):
    title = models.CharField('заголовок',max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='Возможен торг или нет',default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
  

    #метод если запись была создана сегодня то мы отобразим ее зеленым цветом, если не сегодня , то серым
    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():#проверяю что запись была создана сегодня
            created_time =  self.created_at.time().strftime('%H:%M:%S') # 19:30:15
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",
                created_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S') # 04.08.2023 at 19:30:15
    


    @admin.display(description='дата обновления')
    def update_date(self):
        if self.update_at.date() == timezone.now().date():#проверяю что запись была создана сегодня
            update_time =  self.update_at.time().strftime('%H:%M:%S') # 19:30:15
            return format_html(
                "<span style='color:blue; font-weight: bold'>Сегодня в {}</span>",
                update_time
            )
        return self.update_at.strftime('%d.%m.%Y at %H:%M:%S') # 04.08.2023 at 19:30:15





    # представление в виде строки 
    def __str__(self) -> str:
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    # настройки для таблицы
    class Meta:
        db_table = 'advertisments' # переименовали таблицу 











#         from app_advertisements.models import Advertisements                                
#         adv1 = Advertisements (title = 'Молоко', descriptoin = 'Свежее молоко', price = 100, auction = True)   # создаю запись                           
#         adv1.save()           #сохраняю                      
#                                       
# from django.db import connection                              
# connection.queries     # получаю все запросы к sql                            
#                                       
                            