# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    #URL pattern for the order history
    url(
        regex=r'^orderhistory/(?P<username>[\w.@+-]+)/$',
        view=views.UserOrderHistoryView.as_view(),
        name='order_history'
    ),

    #URL pattern for current order
    url(
        regex=r'^currentorder/(?P<username>[\w.@+-]+)/$',
        view=views.UserCurrentOrderView.as_view(),
        name='current_order'
    ),

    #URL pattern for user likes
    url(
        regex=r'^likes/(?P<username>[\w.@+-]+)/$',
        view=views.UserLikeView.as_view(),
        name='likes'
    ),

    #URL pattern for user credit
    url(
        regex=r'^credit/(?P<username>[\w.@+-]+)/$',
        view=views.UserCreditView.as_view(),
        name='credit'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
