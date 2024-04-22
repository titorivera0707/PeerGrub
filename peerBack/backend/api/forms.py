from django import forms
from .models import Listing, Profile, Rating

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'  

class ListingForm(forms.ModelForm):
  class Meta:
    model = Listing
    fields = ['Listing_Title','Listing_Image','Listing_Tags','Listing_Cost','Listing_Calories','Listing_Descr','Listing_Ingredients','allergen_choices']

class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = '__all__'