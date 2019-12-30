from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    if request.method=='POST':
        fs=FileSystemStorage()
        file=request.FILES.get('image')
        save_path=fs.save('static/image'+file.name,file)
        return redirect('/'+ save_path)
    return render(request,'index1.html')