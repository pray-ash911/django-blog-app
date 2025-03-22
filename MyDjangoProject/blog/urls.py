from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, add_post, delete_post, edit_post, post_detail, profile, register
from django.conf.urls.static import static

urlpatterns = [
    path('add_post/', add_post, name='add_post'),
    path("register/", register, name="register"),
    # Built-in login/logout
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path('post/<int:post_id>/edit/',edit_post,name='post_edit'),
    path('post/<int:post_id>/delete/', delete_post, name='post_delete'),
    path('', home, name='home'),  # Home page now uses function-based view
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('profile/', profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)