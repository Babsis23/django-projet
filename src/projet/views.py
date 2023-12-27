from audioop import reverse
from collections import Counter
from django.shortcuts import redirect, render
import base64
import io
import os
import csv
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from matplotlib import figure
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
import os
from django.contrib import messages
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

def get_current_path(request):
    global current_path
    current_path=request.get_full_path()
    return current_path
def home_view(request):
    global chart_type
    chart_type=''
    return render(request, "pages/home.html")

def upload_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        
        if uploaded_file.name.endswith('csv'):
            savefile = FileSystemStorage()
            name=savefile.save(uploaded_file.name,uploaded_file)
            d=os.getcwd()
            file_directory=d+'\media\\'+name
            media_directory=d+'\media\\'
            readfile(file_directory)
            
        else:
            messages.warning(request, "Le fichier n'est pas un csv")  
    return render(request, "pages/upload.html")

def feature_view(request):
    global file_directory, media_directory,d, selected_doc, chart_type
    types=["pie", "bar", "line", "doughnut", "bubble", "polarArea", "radar", "area", "scatter", "mixed"]
    d=os.getcwd()
    media_directory=d+'\media\\'
    hide=False
    csv_files = [file for file in os.listdir(media_directory)]

    if get_current_path != '/feature/' and get_current_path != '/chart/':
        get_current_path(request)
        for i in range(len(current_path.split('/'))):
            if i==2:
                last_digits=current_path.split('/')[i]
                break
        
    for i in range(len(types)):
        if last_digits==types[i]:
            chart_type=types[i]
    print(current_path)
    print(chart_type)
    
    if request.method == 'POST':
        selected_doc=request.POST.get('selected_doc')
        file_directory=d+'\media\\'+selected_doc
        readfile(file_directory)
        return redirect('chart')

    context = {"csv_files": csv_files, "hide":hide, "chart_type":chart_type}
    return render(request, "pages/feature.html", context)

def chart_view(request):
    
    global att1, att2, att3, operation, operation2, file_directory, media_directory, chart_type2, chart_type, chart_type1, nan_mean_columns, valid_mean_columns
    hide=True
    
    csv_files = [file for file in os.listdir(media_directory)]

    # Calculate mean of each column
    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors='coerce')

    # Calculate mean of each column
    means = data.mean()

    # Extract columns where the mean is NaN
    nan_mean_columns = means[means.isnull()].index.to_numpy()

    # Extract columns where the mean is not NaN
    valid_mean_columns = means[means.notnull()].index.to_numpy()
    

    if request.method == 'POST':
        att1=request.POST.get('att1')
        att2=request.POST.get('att2')
        operation=request.POST.get('operation')
        att3=request.POST.get('att3')
        operation2=request.POST.get('operation2')
        if(chart_type=="mixed"):
            chart_type1=request.POST.get('chart_type1')
            chart_type2=request.POST.get('chart_type2')
        return redirect('graph')
        
        
    context={"csv_files": csv_files, "hide":hide, "selected_doc":selected_doc,  "header":header, "chart_type":chart_type, "nan_mean_columns":nan_mean_columns, "valid_mean_columns":valid_mean_columns}

    
    return render(request, "pages/feature.html", context)


def graph_view(request):

    global cType1, cType2, listvalues2

    
    readfile(file_directory)

    data[att2]=pd.to_numeric(data[att2], errors='coerce')
    grouped=data.groupby(att1)[att2].agg(operation)
    
    keys=grouped.index.values
    values=grouped.values
    

    cType=[]
    xAxis=[]
    yAxis=[]
    gTitle=[]

    listvalues2=[]
    cType1=[]
    cType2=[]
    gTitle2=[]

    for i in range(1):
        cType.append(chart_type)
        xAxis.append(att1)
        yAxis.append(att2)
        if operation=='mean':
            gTitle.append("Moyenne")
        elif operation=='sum':
            gTitle.append("Somme")
        elif operation=='median':
            gTitle.append("Mediane")
        elif operation=='max':
            gTitle.append("Maximum")
        elif operation=='min':
            gTitle.append("Minimum")

    if att3:
        data[att3]=pd.to_numeric(data[att3], errors='coerce')
        grouped2=data.groupby(att1)[att3].agg(operation2)
        values2=grouped2.values
        
        for i in range(1):
            cType1.append(chart_type1)
            cType2.append(chart_type2)
            if operation2=='mean':
                gTitle2.append("Moyenne")
            elif operation2=='sum':
                gTitle2.append("Somme")
            elif operation2=='median':
                gTitle2.append("Mediane")
            elif operation2=='max':
                gTitle2.append("Maximum")
            elif operation2=='min':
                gTitle2.append("Minimum")
        
        for i in values2:
            listvalues2.append(i)
        print(cType2, gTitle2)
        print(cType1, gTitle)
        
    print(chart_type)

    print(cType, xAxis, yAxis, gTitle)

    listkeys=[]
    listvalues=[]
    
    for i in keys:
        listkeys.append(i)
    for i in values:
        listvalues.append(i)

    
    csv_files = [file for file in os.listdir(media_directory)]

    context={'listkeys':listkeys,'listvalues':listvalues, "listvalues2":listvalues2 , 'csv_files':csv_files, 'chart_type':chart_type, 'cType':cType, "cType1":cType1, "cType2":cType2, "xAxis":xAxis, "yAxis":yAxis, "gTitle":gTitle, "gTitle2":gTitle2, "att1":att1, "att2":att2, "operation":operation, "selected_doc":selected_doc, "header":header}
    return render(request, "pages/feature.html",context)

def readfile(filename):
    global rows, colums, data, df,header, missing_values
    

    with open(filename, 'r') as file:
        df = csv.reader(file)
        header = next(df)  # Skip the first line (header)
        data = pd.DataFrame(list(df), columns=header)  # Read the remaining rows



    rows=len(data.axes[0])
    colums=len(data.axes[1])

    missingsigns=['?','0','--','NaN']
    null_data = data[data.isnull().any(axis=1)]
    missing_values=len(null_data)
