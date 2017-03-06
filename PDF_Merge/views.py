import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import UploadForm
from .models import FileUpload


# Create your views here

class PDF_Index(FormView):
    form_class = UploadForm
    template = 'pdf_index.html'
    model_class = FileUpload


    # django urls automatically picks the "get" or "post" functions for 'GET' or 'POST' requests
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):  # TODO - can only upload files, cant access them with mergePDF tool
        form = self.form_class(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            for f in files:
                model = self.model_class
                instance = model(file=f)
                instance.save() # saves to 'upload_to' location with crazy name.
            return render(request, self.template, {'form':form, 'success_alert':True})

