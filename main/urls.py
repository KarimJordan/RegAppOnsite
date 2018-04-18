"""RegappOnsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from django.urls.conf import include
from django.conf.urls import url

from .views import HomeView
from allauth.account.views import LoginView, LogoutView

# import viewsets per app
from event.views import EventsViewSet
from layout.views import LayoutViewSet
from guest.views import GuestViewSet
from raffler.views import RafflerViewSet

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar

router = routers.SimpleRouter()
router.register(r'events', EventsViewSet)
router.register(r'layouts', LayoutViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'rafflers', RafflerViewSet)

urlpatterns = [

    url(r'^$', LoginView.as_view(), name='login'),
    url('admin/', admin.site.urls),
    # url('login/', LoginView.as_view(), name='login'),
    path('guests/fields/<int:pk>/', GuestViewSet.as_view({'post': 'fields'}), name='fields'),
    path('guest/info/<int:pk>/', GuestViewSet.as_view({'post': 'update_info'}, name='update_info')),
    path('guest/delete/<int:pk>/', GuestViewSet.as_view({'post': 'delete_info'}, name='delete_info')),
    path('events/upload/<int:pk>/', EventsViewSet.as_view({'post', 'upload_excel'}), name='upload_excel'),
    url('/guests/upload/', EventsViewSet.as_view({'post': 'upload'}), name='upload'),
    url('api/events/', EventsViewSet.as_view({'get': 'events_list'}), name='events_list'),
    url('api/guest_events/', EventsViewSet.as_view({'get': 'guest_events'}), name='guest_events'),
    url('api/field_value_list/', RafflerViewSet.as_view({'get': 'field_value_list'}), name='field_value_list'),
    path('api/layouts/events/<int:pk>/', LayoutViewSet.as_view({'get': 'layout_list'}), name='layout_list'),
    path('api/layouts/<int:pk>/', LayoutViewSet.as_view({'get', 'layout_data'}), name='layout_data'),
    path('api/guests/<int:pk>/', GuestViewSet.as_view({'get': 'guest_list'}), name='guest_list'),
    path('api/add_guest/<int:pk>/', GuestViewSet.as_view({'post': 'guest_add'}), name='guest_add'),
    # add url for serializations
    url(r'^', include(router.urls)),
    # url(r'^api/', include(router.urls)),

    # All auth
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^accounts/', include('allauth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.USE_DEBUG_TOOLBAR:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
