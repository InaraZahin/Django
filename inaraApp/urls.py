from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('new', views.new_index, name='new_index'),
path('about', views.about, name='about'),
path('blog', views.blog,  name='blog'),
path('contact', views.contact, name='contact'),
path('services', views.services, name='services'),
path('work', views.work, name='work'),
path('work-single', views.worksingle, name='work-single'),
# path('about_us', views.about_us, name='about_us'),
# path('testimonials', views.testimonials, name='testimonials'),
# path('contact_us', views.contact_us, name='contact_us'),
path('contact/', views.ContactView.as_view(), name="contact"),

# path('createpost/', views.createpost, name="createpost"),
# path('createmessage/', views.createmessage, name="createmessage"),
path('post/', views.createpost, name='createpost'),
]
