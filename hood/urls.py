from django.urls import re_path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns=[
    re_path(r'^$',views.index,name='Index'),
    re_path(r'^blog',views.blog, name='blog'),
    re_path(r'^view/blog/(\d+)',views.view_blog,name='view_blog'),
    re_path(r'^my-profile/',views.my_profile, name='my-profile'),
    re_path(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    re_path(r'^new/blogpost$',views.new_blogpost, name='new-blogpost'),
    re_path(r'^create/profile$',views.create_profile, name='create-profile'),
    re_path(r'^update/profile$',views.update_profile, name='update-profile'),
    re_path(r'^search/',views.search_results, name='search_results'),
    re_path(r'accounts/',include('django_registration.backends.one_step.urls')),
    re_path(r'accounts/', include('django.contrib.auth.urls')),
    re_path(r'^login/', auth_views.LoginView.as_view(), {"next_page": '/'}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

