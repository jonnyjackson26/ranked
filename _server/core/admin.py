from django.contrib import admin
from .models import PhysicalAttributes

@admin.register(PhysicalAttributes)
class PhysicalAttributesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'height', 
        'weight', 
        'fastest_40_yard_dash', 
        'bench_press_max', 
        'deadlift_max', 
        'squat_max', 
        'wingspan', 
        'vertical_jump_height', 
        'resting_heart_rate', 
        'vo2_max', 
        'dominant_hand', 
        'eye_color', 
        'hair_color'
    )
