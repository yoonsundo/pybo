from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 , redirect
from .models import CodeList 
 
@login_required(login_url='common:login') 
def index(request):  
    combo_list = CodeList.objects.filter(codegrpcd='cc100').order_by('codeseq') 
     
    context = {'combo_list': combo_list } 
    return render(request, 'exam/exam.html', context) 


def findExamList(request):
    """
    sales 목록 출력
    """
    # 입력 인자
    search_mode = request.GET.get('search_mode')
    print(search_mode)
    sales_list = CodeList.objects.filter(codegrpcd='cc101').order_by('codeseq')
    combo_list = CodeList.objects.filter(codegrpcd='cc100').order_by('codeseq') 
    sales_list = sales_list.filter(
            upcodecd=search_mode  # 제목 검색 
        )
    print(sales_list)
    context = {'sales_list': sales_list
               ,'combo_list': combo_list
               ,'search_mode' : search_mode}
    return render(request, 'exam/exam.html', context)