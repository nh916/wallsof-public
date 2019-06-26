from django.urls import path
from wallOf import views as WallOf_Views

urlpatterns = [
    path('secretes/', WallOf_Views.secreteView, name='secretes'),

    path('frustrations/', WallOf_Views.index, name='frustrations'),
    path('', WallOf_Views.index, name='index.html'),

    path('redirected/', WallOf_Views.redirect_back, name='redirect_back'),
    path('wisdom/', WallOf_Views.advice_view, name='advice'),

    # path('happiness', WallOf_Views.happiness, name='happiness')

    # path('', WallOfViews.index, name='index.html'),
    # path('', WallOfViews.create_post.as_view(), name='index.html'),
]
