from django.conf.urls import patterns, url
   
urlpatterns = patterns('blog.views',                     
                       url(r'^welcome/$', 'home'),
                       url(r'^data/$', 'data'),
                       #url(r'^object/(?P<id_object>\d+)/$', 'view_object'), #object view
                       url(r'^object/(?P<id>\d+)-(?P<slug>.+)/$', 'read'), #object view
                       url(r'^object/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'view_object_date'), #object view with view_object_date
                       url(r'^$', 'test_html'),#test html object with template
                       url(r'^index.html$', 'generate_index'),#test html object with template
                       url(r'^form/$', 'form_contact'),
                       url(r'^new-contact/$', 'new_comment'),
                       url(r'^view-contacts/$', 'view_comment'),
                       url(r'^subscribe/$', 'subscribe'),
                       url(r'^connexion/$', 'connexion'),
                       url(r'^deconnexion/$', 'deconnexion'),
                       url(r'^alert/$', 'sign_in_first'),
                       url(r'^git/$', 'git_form'),
                       )