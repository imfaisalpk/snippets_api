from django.conf.urls import url
from django.contrib import admin

from snippets import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/api/$',views.SnippetList.as_view(), name="snippets_list"),
    url(r'^snippets/api/(?P<pk>\d+)/$',views.SnippetDetail.as_view(), name="snippets_detail"),
    url(r'^users/api/$',views.UserList.as_view(), name="users_list"),
    url(r'^users/api/(?P<pk>\d+)/$',views.UserDetail.as_view(), name="users_detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
