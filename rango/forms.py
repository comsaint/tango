from django import forms
from rango.models import Page, Category

# a form for the class 'Category'
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    #specified the widgets that we wish to use for each field to be displayed via 'widget'
    #do not allow user access to property 'view' by 'HiddenInput', yet supplies an 'initial' value of '0' to the model
    #REMEMBER: even if a field is hidden, we have to include it in the form! ...
    #except if a default value is provided in the model
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False) # set this to be not required, because it will be populated by the save() method in themodel

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',) #the 'fields' property specifies fields to be included


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    def clean(self):
        """
        Clean user's input URL - append 'http://' in front of the address if necessary
        Override clean() method in ModelForm class.
        """
        cleaned_data = self.cleaned_data #Form data is obtained from the ModelForm dictionary attribute 'cleaned_data'
        url = cleaned_data.get('url') #get the url field - we want to check this

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            
        # We MUST always end the clean() method by returning the reference to the cleaned_data dictionary. 
        # Otherwise we will get some really frustrating errors!
        return cleaned_data
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',) #this specifies fields to be excluded
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
