from django.contrib import admin
from .models import Question,SideMenuList,SideSubMenuList,Answer

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
class SideMenuListAdmin(admin.ModelAdmin):
    search_fields = ['title']
class SSideSubMenuListAdmin(admin.ModelAdmin):
    search_fields = ['title']
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Answer, AnswerAdmin) 
admin.site.register(Question, QuestionAdmin)
admin.site.register(SideMenuList, SideMenuListAdmin)
admin.site.register(SideSubMenuList, SSideSubMenuListAdmin)