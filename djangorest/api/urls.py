from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    re_path(r'^yamb/$', CreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
