from django.shortcuts import render
import json

# Create your views here.
def index(request):
    """View function for home page of site."""
    json_data = open('myapp/static/json/vegetables.json')
    data = json.load(json_data)
    json_data.close()
    lst = data['vegetables']

    # Generate counts of some of the main objects
    vegetable_name = lst['name']
    availability = lst['availability']

    # Available books (status = 'a')
    mrp = lst['mrp']

    # The 'all()' is implied by default.

    context = {
        'vegetable_name': vegetable_name,
        'availability': availability,
        'mrp': mrp,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
