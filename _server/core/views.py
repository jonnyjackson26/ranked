from django.shortcuts import render
from django.conf  import settings
import json
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Load manifest when server launches
MANIFEST = {}
if not settings.DEBUG:
    f = open(f"{settings.BASE_DIR}/core/static/manifest.json")
    MANIFEST = json.load(f)

# Create your views here.
@login_required
def index(req):
    context = {
        "asset_url": os.environ.get("ASSET_URL", ""),
        "debug": settings.DEBUG,
        "manifest": MANIFEST,
        "js_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["file"],
        "css_file": "" if settings.DEBUG else MANIFEST["src/main.ts"]["css"][0]
    }
    return render(req, "core/index.html", context)


from .models import PhysicalAttributes
@login_required
@csrf_exempt
def save_physical_attributes(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        user = request.user

        try:
            attributes = user.physical_attributes
        except PhysicalAttributes.DoesNotExist:
            attributes = PhysicalAttributes(user=user)

        # Convert empty strings to None
        for field, value in data.items():
            if value == "":
                data[field] = None

        # Update or create attributes with safe defaults
        attributes.height = data.get('height') or attributes.height
        attributes.weight = data.get('weight') or attributes.weight
        attributes.fastest_40_yard_dash = data.get('fastest_40_yard_dash') or attributes.fastest_40_yard_dash
        attributes.bench_press_max = data.get('bench_press_max') or attributes.bench_press_max
        attributes.deadlift_max = data.get('deadlift_max') or attributes.deadlift_max
        attributes.squat_max = data.get('squat_max') or attributes.squat_max
        attributes.wingspan = data.get('wingspan') or attributes.wingspan
        attributes.vertical_jump_height = data.get('vertical_jump_height') or attributes.vertical_jump_height
        attributes.resting_heart_rate = data.get('resting_heart_rate') or attributes.resting_heart_rate
        attributes.vo2_max = data.get('vo2_max') or attributes.vo2_max
        attributes.dominant_hand = data.get('dominant_hand') or attributes.dominant_hand
        attributes.eye_color = data.get('eye_color') or attributes.eye_color
        attributes.hair_color = data.get('hair_color') or attributes.hair_color

        attributes.save()

        return JsonResponse({'success': True, 'message': 'Physical attributes saved!'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)



@login_required
def get_users_physical_attributes(request):
    try:
        # Fetch the physical attributes of the logged-in user
        attributes = request.user.physical_attributes
    except PhysicalAttributes.DoesNotExist:
        return JsonResponse({'error': 'Physical attributes not found'}, status=404)

    # Prepare data to return as JSON
    data = {
        'height': attributes.height,
        'weight': attributes.weight,
        'fastest_40_yard_dash': attributes.fastest_40_yard_dash,
        'bench_press_max': attributes.bench_press_max,
        'deadlift_max': attributes.deadlift_max,
        'squat_max': attributes.squat_max,
        'wingspan': attributes.wingspan,
        'vertical_jump_height': attributes.vertical_jump_height,
        'resting_heart_rate': attributes.resting_heart_rate,
        'vo2_max': attributes.vo2_max,
        'dominant_hand': attributes.dominant_hand,
        'eye_color': attributes.eye_color,
        'hair_color': attributes.hair_color,
    }

    return JsonResponse(data)


@login_required
def get_users_stats(request):
    dummy = [
    {
        "title": "Bench Press Max",
        "description": "Congrats! You're in the 90th percentile for your bench press max!",
        "shareMessage": "I'm in the 90th percentile for my bench press max! Check out my amazing stats!"
    },
    {
        "title": "Height",
        "description": "You're the tallest female with blue eyes and brown hair!",
        "shareMessage": "I'm the tallest female with blue eyes and brown hair! Celebrate my unique stats!"
    }
    ]
    return JsonResponse(dummy, safe=False)



from .models import ICan
@login_required
@csrf_exempt
def save_i_can(request):
    if request.method == "POST":
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            print("Received data:", data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        # Get the user or create a default instance
        user = request.user  # Assuming user is logged in

        # Check if there's already a ICan instance for the user
        try:
            can_you = ICan.objects.get(user=user)
        except ICan.DoesNotExist:
            can_you = ICan(user=user)

        # Update fields dynamically based on incoming data
        for field, value in data.items():
            if hasattr(can_you, field):
                setattr(can_you, field, value)

        # Attempt to save the instance
        try:
            can_you.save()
        except Exception as e:
            return JsonResponse({'error': f"Error saving data: {str(e)}"}, status=500)

        # Return a success response
        return JsonResponse({'success': True, 'message': 'Data saved successfully!'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)




@login_required
def get_users_i_cans(request):
    # Get the logged-in user
    user = request.user

    try:
        # Get the user's ICan instance
        can_you = ICan.objects.get(user=user)

        # Create a dictionary of the boolean fields
        user_i_cans = {
            "solve_rubiks_cube": can_you.solve_rubiks_cube,
            "dunk_basketball": can_you.dunk_basketball,
            "do_a_backflip": can_you.do_a_backflip,
            "juggle_three_balls": can_you.juggle_three_balls,
            "ride_a_unicycle": can_you.ride_a_unicycle,
            "do_a_cartwheel": can_you.do_a_cartwheel,
            "swim": can_you.swim,
            "do_10_push_ups": can_you.do_10_push_ups,
            "do_a_muscle_up": can_you.do_a_muscle_up,
            "touch_your_toes": can_you.touch_your_toes,
            "spin_a_basketball_on_your_finger": can_you.spin_a_basketball_on_your_finger,
            "drive_a_car": can_you.drive_a_car,
        }

        # Return the user's ICan data as JSON
        return JsonResponse({'success': True, 'data': user_i_cans})

    except ICan.DoesNotExist:
        return JsonResponse({'error': 'User ICan instance not found'}, status=404)