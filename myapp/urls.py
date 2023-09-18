from django.urls import path
from .views import (MultimediaViews,
                    InfoPageView,
                    setLanguage,
                    )

urlpatterns = [
    path('setLang/<str:lang>', setLanguage),
    path('info/', InfoPageView.as_view(), name='info'),
    path('', MultimediaViews.as_view(), name='home'),
]


