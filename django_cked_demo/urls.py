from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_cked_demo.cked_demo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_cked_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.ArticleList.as_view(), name='articles-list'),
    url(r'^text-(?P<id>\d+)/$', views.ArticleDetail.as_view(), name='article-detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cked/', include('cked.urls')),
)
