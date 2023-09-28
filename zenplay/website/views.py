from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})
 
def meetings(request):
    return render(request, 'meetings.html', {})
 
def meetingdetails(request):
    return render(request, 'meetingdetails.html')   
