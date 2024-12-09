from django.contrib import admin
from .models import PhysicalAttributes
from .models import ICan

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



@admin.register(ICan)
class ICanAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'solve_rubiks_cube',
        'dunk_basketball',
        'do_a_backflip',
        'juggle_three_balls',
        'ride_a_unicycle',
        'do_a_cartwheel',
        'swim',
        'do_10_push_ups',
        'do_a_muscle_up',
        'touch_your_toes',
        'spin_a_basketball_on_your_finger',
        'drive_a_car',
    )