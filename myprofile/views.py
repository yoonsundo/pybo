from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import pandas as pd 
import requests 
import matplotlib.pyplot as plt
# 필요한 모듈 import 하기 
import plotly
import plotly.graph_objects as go
import plotly.express as px 
 
@login_required(login_url='common:login') 
def index(request):  
    
    context = {'stock_list': "ss" }  
    return render(request, 'myprofile/profile.html', context) 
 