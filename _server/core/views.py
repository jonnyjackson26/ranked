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
@csrf_exempt
@login_required
def save_physical_attributes(request):
    if request.method == "POST":
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        user = request.user
        print(data)  # Check incoming data

        # Check if the user already has physical attributes
        try:
            attributes = user.physical_attributes
        except PhysicalAttributes.DoesNotExist:
            attributes = PhysicalAttributes(user=user)

        # Update or create attributes
        attributes.height = int(data.get('height', 0))
        attributes.weight = int(data.get('weight', 0))
        attributes.fastest_40_yard_dash = float(data.get('fastest_40_yard_dash', 0))
        attributes.bench_press_max = int(data.get('bench_press_max', 0))
        attributes.deadlift_max = int(data.get('deadlift_max', 0))
        attributes.squat_max = int(data.get('squat_max', 0))
        attributes.wingspan = int(data.get('wingspan', 0))
        attributes.vertical_jump_height = float(data.get('vertical_jump_height', 0))
        attributes.resting_heart_rate = int(data.get('resting_heart_rate', 0))
        attributes.vo2_max = data.get('vo2_max')
        attributes.dominant_hand = str(data.get('dominant_hand'))
        attributes.eye_color = str(data.get('eye_color'))
        attributes.hair_color = str(data.get('hair_color'))

        # Save the data
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


