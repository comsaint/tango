from django.shortcuts import render

#from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

# Create your views here.

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name #add data into context_dict

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # i.e. render the {{boldmessage}} field etc. in 'index.html' with the values here.
    #context_dict = {'boldmessage': "I am bold font from the context",
    #                'h2_message' : "... And I am another message!"
    #}

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list_mostlikes = Category.objects.order_by('-likes')[:5]
    category_list_mostviews = Category.objects.order_by('-views')[:5]
    # query the Category model to retrieve the top five categories (both most liked or viewed).
    # '-' for descending order
    
    context_dict = {'categories_mostlikes': category_list_mostlikes,
                    'categories_mostviews': category_list_mostviews
                    }
    #pass a reference to the list (stored as variable category_list) to the dictionary, context_dict
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context_dict) #remember to mention 'context_dict' in here

def about(request):
    #output = r'Rango says here is the about page. <br/> <a href="/rango/">Index</a>'
    #return HttpResponse(output)
    return render(request, 'rango/about.html')

def add_category(request):
    """
    add_category() view function can handle three different scenarios:
    1. showing a new, blank form for adding a category;
    2. saving form data provided by the user to the associated model, and rendering the Rango homepage; and
    3. if there are errors, redisplay the form with error messages.
    """
    # A HTTP POST? Determine if it was a HTTP GET or POST
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    # Note: the 'category_name_slug' field was passed by the ...(?P<category_name_slug>...) matching field in urls.py
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                #return category(request, category_name_slug)
                # Said and done!
                # To enable the reverse method, I modified the main urls.py to include a namespace 'rango'
                # 'rango:category' calls the 'category' method in 'views.py' in namespace 'rango',
                # with argument 'category_name_slug' as required by the method
                return HttpResponseRedirect(reverse('rango:category', args=(category_name_slug,)))
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat, 'category_name_slug':category_name_slug}

    return render(request, 'rango/add_page.html', context_dict)