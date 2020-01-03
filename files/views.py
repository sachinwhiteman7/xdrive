from django.shortcuts import render, redirect
from django.views import View

from .forms import FileUploadForm
from .models import FileUpload


class FileView(View):
    template_name = "files/list.html"

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("accounts:login")
        files = FileUpload.objects.filter(user=request.user)
        return render(request, self.template_name, {"files": files, "form": FileUploadForm})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            file_name, file_type = file.name.rsplit(".", 1)
            file_object = FileUpload(file=file, file_name=file_name, file_type=file_type, user=request.user)
            file_object.save()
        files = FileUpload.objects.filter(user=request.user)
        return render(request, self.template_name, {"files": files, "form": FileUploadForm})
