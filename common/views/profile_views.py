from django.db.models import F, Count
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from common.forms import UserForm, PasswordResetForm , ProfileForm

from pybo.models import Question, Answer 
from common.models import Profile 

@login_required(login_url='common:login')
def profile_base(request, user_id):
    """
    프로필 기본정보
    """
    if request.method == "POST": 
        print(request.POST)
        print(user_id)
        user = get_object_or_404(User, pk=user_id)  
        user.profile.name = request.POST['name']
        user.profile.address = request.POST['address']
        user.profile.save()   
    else:
        user = get_object_or_404(User, pk=user_id)
     
    context = {'profile_user': user, 'profile_type': 'base' }
    return render(request, 'common/profile/profile_base.html', context)


class ProfileObjectListView(ListView):
    """
    프로필 목록 추상 클래스 뷰
    """
    paginate_by = 10

    class Meta:
        abstract = True

    def get_queryset(self):
        print(self)
        print(self.kwargs)
        self.profile_user = get_object_or_404(User, pk=self.kwargs['user_id'])
        self.so = self.request.GET.get('so', 'recent')  # 정렬기준
        object_list = self.model.objects.filter(author=self.profile_user)
        # 정렬 
        
        object_list = Question.objects.order_by('create_date')
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'profile_user': self.profile_user,
            'profile_type': self.profile_type,
            'so': self.so
        })
        return context

class ProfileQuestionListView(ProfileObjectListView):
    """
    작성한 질문 목록
    """
    model = Question
    template_name = 'common/profile/profile_question.html'
    profile_type = 'question'