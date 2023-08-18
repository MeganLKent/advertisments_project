from django .urls import path
from .views import index, top_sellers, advertisment_post

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('advertisment_post/', advertisment_post, name = 'adv-post')
]