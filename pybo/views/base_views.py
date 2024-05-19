# 기본관리
# index, detail

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from ..models import Question, Answer

@login_required(login_url='common:login') 
def index(request):  
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('create_date') 
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj , 'page': page, 'kw': kw}  
    return render(request, 'pybo/question_list.html', context)

@login_required(login_url='common:login')
def detail(request, question_id):
    page = request.GET.get('page', '1')  # 페이지 
   
    answer_list = Answer.objects.filter(question=question_id).order_by('create_date')   
    paginator = Paginator(answer_list, 3)  # 페이지당 10개씩 보여주기  
    page_obj = paginator.get_page(page) 
     
    # print('----sdsdsdsds---')  
    # print(page_obj)  
    question = get_object_or_404(Question, pk=question_id)
       
    context = {'question': question, 'answer_list': page_obj}
    return render(request, 'pybo/question_detail.html', context)   

@login_required(login_url='common:login')
def sideMenuGet(request):
    sideMenu_list = SideMenuList.objects.order_by('-seq') 
    context = {'sideMenu_list': sideMenu_list}
    return redirect('pybo:index') 
