from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='Index'),
    path('blog',views.blog, name='blog'),
    path('view/blog/(\d+)',views.view_blog,name='view_blog'),
    path('my-profile/',views.my_profile, name='my-profile'),
    # path('user/(<username>\)',views.user_profile,name='user-profile'),
    path('new/blogpost',views.new_blogpost, name='new-blogpost'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('update/profile',views.update_profile, name='update-profile'),
    path('search/',views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
