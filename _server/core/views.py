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
def physical_attributes(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            PhysicalAttributes.objects.create(
                height=data["height"],
                weight=data["weight"],
                dash=data["dash"],
                bench_press=data["benchPress"],
                deadlift=data["deadlift"],
                squat=data["squat"],
                wingspan=data["wingspan"],
                vertical_jump=data["verticalJump"],
                heart_rate=data["heartRate"],
                vo2_max=data.get("vo2Max"),
                dominant_hand=data["dominantHand"],
                eye_color=data["eyeColor"],
                hair_color=data["hairColor"],
            )
            return JsonResponse({"message": "Data saved successfully!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=400)


