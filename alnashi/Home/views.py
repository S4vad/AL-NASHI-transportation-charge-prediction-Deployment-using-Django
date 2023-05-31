from django.shortcuts import render
from joblib import load
import sklearn
model=load("C:/Users/savad/Desktop/al_nashi/savedmodels/model.joblib")

# Create your views here.

def frm(From):
    if From=='Riyadh':
        d=0
    return d

def dtn(Destination):
    if Destination=='MADEENA':
        d=14
    elif Destination=='BURIDHA':
        d=5
    elif Destination=='JEDDAH':
        d=11      
    elif Destination=='NAJRAN':
        d=17
    elif Destination=='YANBU':
        d=24       
    elif Destination=='AL JOUF':
        d=1   
    elif Destination=='ARAR':
        d=4
    elif Destination=='HAIL':
        d=10        
    elif Destination=='QURIYATH':
        d=19        
    elif Destination=='HAFER AL BATHEN':
        d=9         
    elif Destination=='ABAHA':
        d=0         
    elif Destination=='TABUK':
        d=20       
    elif Destination=='MAKKAH':
        d=16         
    elif Destination=='DAWADMI':
        d=7        
    elif Destination=='AL KHARAJ':
        d=2         
    elif Destination=='WADI DAWASSIR (DEDICATED)':
        d=23       
    elif Destination=='NAJRAN (DEDICATED)':
        d=18 
    elif Destination=='DAWADMI (DEDICATED)':
        d=8
    elif Destination=='DAMMAM':
        d=6
    elif Destination=='LOCAL TRANSFER':
        d=13
    elif Destination=='MAJMA':
        d=15
    elif Destination=='TAIF':
        d=21
    elif Destination=='JIZAN':
        d=12
    elif Destination=='AL QASEEM':
        d=3
    elif Destination=='WADI DAWASSIR':
        d=22
    return d

def vt(Vehicle_Type):
    if Vehicle_Type=='FSR':
        d=1
    elif Vehicle_Type=='DYNA':
        d=0

    return d


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def prediction(request):
    if request.method=='POST':
        From=request.POST['From']
        Destination=request.POST['Destination']
        Vehicle_Type=request.POST['Vehicle_Type']
        
        
        list=[frm(From),dtn(Destination),vt(Vehicle_Type)]
        
        y_pred=model.predict([list])
        return render(request,'prediction.html',{'word':'The predicted Transportation Charge is :','result':y_pred})
    return render(request,'prediction.html')
def contact(request):
    return render(request,'contact.html')
    