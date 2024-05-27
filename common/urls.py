"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from common.views  import account_views, profile_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', account_views.logout_view, name='logout'),
    path('signup/', account_views.signup, name='signup'),
 
	# 비밀번호 초기화
	path('password_reset/', account_views.PasswordResetView.as_view(), name='password_reset'), 
	path('password_reset/done/', account_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', account_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

     # 프로필
    path('profile/base/<int:user_id>/', profile_views.profile_base, name='profile_base'),
    path('profile/question/<int:user_id>/', profile_views.ProfileQuestionListView.as_view(), name='profile_question'),
    # path('profile/answer/<int:user_id>/', profile_views.ProfileAnswerListView.as_view(), name='profile_answer'),
    # path('profile/comment/<int:user_id>/', profile_views.ProfileCommentListView.as_view(), name='profile_comment'),
    # path('profile/vote/<int:user_id>/', profile_views.ProfileVoteListView.as_view(), name='profile_vote'),
]