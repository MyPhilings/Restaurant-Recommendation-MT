import json
from django.shortcuts import render

# Forms
from . forms import restaurantForm

#Requests
from . requests import currency, language, typeAhead, search, details, photos, reviews
 
# Create your views here.
def home(request):
    
    restaurant_typeAhead_response = {}
    restaurant_intypeAhead_response = {}
    
    if request.method == 'POST':
        restaurant_input = restaurantForm(request.POST)
        
        if restaurant_input.is_valid():
            restaurant_name = restaurant_input.cleaned_data['restaurant_input'].lower().split()
            restaurant_typeAhead_response = typeAhead(restaurant_name)
            
            data_list = restaurant_typeAhead_response['results']['data']

            #This is our error catching since any input is always accepted
            if len(data_list) == 0:
                print("No Results Found.")
                restaurant_input = restaurantForm()

            for item in data_list:

                result_object = item['result_object']
                
                location_id = result_object['location_id']

            restaurant_intypeAhead_response = search(location_id)
            # print(location_id)
            # print(restaurant_intypeAhead_response)


    else:
        restaurant_input = restaurantForm()
    
    context ={
        'restaurant_input': restaurant_input,
        'typeAhead': restaurant_typeAhead_response,
        'restaurant_in_typeAhead': restaurant_intypeAhead_response
    }

    return render(request, 'homepage/basics.html', context = context)