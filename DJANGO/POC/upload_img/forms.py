from django import forms
# TODO : a tried
from django.forms import TextInput, Select, DateInput, FileInput, CheckboxInput, TimeInput, CheckboxSelectMultiple, modelformset_factory, Textarea

from .models import Image

class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image1', )

    image1 = forms.ImageField(label='Image', required=False,
                                    error_messages ={'invalid': "Importer uniquement un fichier .png ou .jpg"},
                                    widget=FileInput(attrs={'class': 'custom-file-input',}))    
                                                        # '@change': 'previewImage'}))    
    # remove_profile_image = forms.BooleanField(label="Supprimer l'avatar", required=False, 
    #                                     widget=CheckboxInput(attrs={'class': 'custom-control-input'}))

    def save(self, commit=False, *args, **kwargs):
      image = super().save(commit=False, *args, **kwargs)
      image.image1 = self.cleaned_data['image1']
      image.save()
      return image
        
        # if self.cleaned_data['remove_profile_image']:
        #     default_image = user_profile._meta.get_field('profile_image').get_default()
        #     user_profile.profile_image = default_image
        #     user_profile.save()
        # else:
        #     user_profile.profile_image = self.cleaned_data['profile_image']
        #     user_profile.save()
        # return user_profile