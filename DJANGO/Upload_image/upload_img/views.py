from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView, UpdateView #, DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import *
# Create your views here.


class ImageCreateView(CreateView):
  def get(self, request):
    # mettre tout ca dans un try 
    new_i = Image.objects.create()
    new_i.save()
    return HttpResponseRedirect(reverse('upload_img:image_update', args=(new_i.pk,) ) )


class ImageUpdateView(UpdateView):
  model = Image
  template_name = 'upload_img/image_update.html'
  form_class = ImageUpdateForm

  def upload_file(request):
    if request.method == 'POST':
      form = ImageUpdateForm(request.POST, request.FILES)
      if form.is_valid():
        instance = Image(image1=request.FILES['image1'])
        instance.save()
        return HttpResponseRedirect(self.get_success_url())
        # return HttpResponseRedirect('upload_img:image_update')
    else:
      form = UploadFileForm()
    return render(request, 'www.google.fr', {'form': form})

  def get_success_url(self):
    return reverse('upload_img:image_update', args=(self.object.pk,))        