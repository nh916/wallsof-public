from django.urls import path, re_path
from wallOf import views as WallOf_Views


urlpatterns = [
    path('', WallOf_Views.spam_view, name='index.html'),

    re_path(r'secrets?/$(?i)', WallOf_Views.secretView, name='secrets'),

    path('frustrations/', WallOf_Views.frustrations, name='frustrations'),

    path('redirected/', WallOf_Views.redirect_back, name='redirect_back'),

    path('wisdom/', WallOf_Views.advice_view, name='wisdom'),

    path('joy/', WallOf_Views.joy_view, name='joy'),

    path('spam/', WallOf_Views.spam_view, name='spam'),

    path('congrats/', WallOf_Views.graduation_view, name='congrats'),

    # path('happiness', WallOf_Views.happiness, name='happiness')
]
