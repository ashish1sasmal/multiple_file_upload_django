from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def upload(request):
    context={'flag':0}
    if request.method == 'POST' and request.FILES['myfile']:
        files = request.FILES.getlist('myfile')
        for i in files:
            fs = FileSystemStorage()
            filename = fs.save(i.name, i)
        print("ALL files saved!")
        context['flag']=1
        return render(request, 'upload/index.html',context)
    return render(request, 'upload/index.html',context)
