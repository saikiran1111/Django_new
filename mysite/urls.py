
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from mysite.loginform import views 
from django.conf.urls.static import static

urlpatterns = [
	path('',views.home,name="home"),

	path('bot',views.bot,name="bot"),
	path('finance',views.logo,name="logo"),
	
	path('index',views.index,name="index"),
	path('exchange',views.exchange,name="exchange"),
	
	path('signup',views.signup,name="signup"),
	path('^oauth/', include('social_django.urls', namespace='social')),
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    