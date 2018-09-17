import xadmin
from django.conf.urls import url, include

from apps.home import views

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    # 设置默认首页
    url('^$', views.index),
    url('account/', include('apps.account.urls')),
    url('shop_detail/', include('apps.shop_detail.urls')),
    url('order/', include('apps.order.urls')),
    url('cate_sort/', include('apps.cate_sort.urls')),
    url('cart/', include('apps.cart.urls')),
    url('home/', include('apps.home.urls')),
    url('pay/', include('apps.pay.urls')),

]
