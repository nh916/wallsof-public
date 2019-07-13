from django.urls import path, re_path
from wallOf import views as WallOf_Views


urlpatterns = [
    re_path(r'secrets?/$(?i)', WallOf_Views.secreteView, name='secretes'),

    path('frustrations/', WallOf_Views.frustrations, name='frustrations'),
    path('', WallOf_Views.frustrations, name='index.html'),

    path('redirected/', WallOf_Views.redirect_back, name='redirect_back'),
    path('wisdom/', WallOf_Views.advice_view, name='wisdom'),

    # path('happiness', WallOf_Views.happiness, name='happiness')

    # path('', WallOfViews.index, name='index.html'),
    # path('', WallOfViews.create_post.as_view(), name='index.html'),
]
