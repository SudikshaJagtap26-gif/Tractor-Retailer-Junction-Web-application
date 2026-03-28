import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from Base_App.models import AboutUs, Feedback, ItemList, Items, Offer
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.conf import settings
from datetime import date

def add_to_cart(request):
    if request.method == 'POST' and request.user.is_authenticated:
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Items, id=item_id)
        
        print(f'Item ID: {item_id}')  # Debug print
        print(f'Item: {item.Item_name}, Price: {item.Price}')  # Debug print

        # Retrieve or initialize the cart from the session
        cart = request.session.get('cart', {})
        print(f'Cart before update: {cart}')  # Debug print

        # Update the cart
        if item_id in cart:
            cart[item_id]['quantity'] += 1
        else:
            cart[item_id] = {
                'name': item.Item_name,
                'price': item.Price,
                'quantity': 1
            }

        request.session['cart'] = cart
        print(f'Cart after update: {cart}')  # Debug print

        return JsonResponse({'message': 'Item added to cart', 'cart': cart})
    else:
        print('Invalid request')  # Debug print
        return JsonResponse({'error': 'Invalid request'}, status=400)

class LoginView(AuthLoginView):
    template_name = 'login.html'
    def get_success_url(self):
        # Check if the user is an admin
        if self.request.user.is_staff:
            return reverse_lazy('admin:index')  # Redirects to the Django admin panel
        return reverse_lazy('Home')  # Redirects to the home page if not an admin

def LogoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('Home')  # Redirect to a page after logout, e.g., the home page

def SignupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('Home')
        else:
            messages.error(request, 'Error during signup. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form, 'tab': 'signup'})


def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all().order_by('-id')[:5]

    offer = Offer.objects.filter(
        active=True,
        start_date__lte=date.today(),
        end_date__gte=date.today()
    ).first()

    return render(request, 'home.html',{
        'items': items,
        'list': list,
        'review': review,
        'offer': offer
    })


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return redirect('tractor_collection')



def visit_page(request):
    return render(request, 'book_table.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })

def FeedbackView(request):
    feedback_list = Feedback.objects.all().order_by('-id')

    if request.method == 'POST':
        name = request.POST.get('User_name')
        feedback = request.POST.get('Description')
        rating = request.POST.get('Rating')
        image = request.FILES.get('Selfie')

        if name != '':
            feedback_data = Feedback(
                User_name=name,
                Description=feedback,
                Rating=rating,
                Image=image
            )
            feedback_data.save()

            # WhatsApp message
            whatsapp_message = f"""
New Feedback Received

Name: {name}
Rating: {rating}
Feedback: {feedback}
"""

            whatsapp_url = f"https://wa.me/919423587536?text={whatsapp_message}"

            return redirect(whatsapp_url)

    return render(request, 'feedback.html', {'reviews': feedback_list})
def tractor_collection(request):
    tractors = Items.objects.all()
    categories = ItemList.objects.all()

    tractor_list = []
    for t in tractors:
        tractor_list.append({
            "id": t.id,
            "name": t.Item_name,
            "brand": t.Category.Category_name,
            "on_road_price": t.On_Road_Price,
            "fixed_price": t.Fixed_Price,
            "images": [
                t.Image.url if t.Image else "",
                t.Image2.url if t.Image2 else "",
                t.Image3.url if t.Image3 else "",
                t.Image4.url if t.Image4 else "",
                t.Image5.url if t.Image5 else "",
            ],
            "description": t.description,
            "Engine": t.Engine,
            "Power": t.Power,
            "No_of_cylinder": t.No_of_cylinder,
            "Gear_box": t.Gear_box,
            "phone": t.phone,
            "location": t.location,
        })

    context = {
        "tractors_json": json.dumps(tractor_list),
        "categories": categories
    }

    return render(request, "collection.html", context)
