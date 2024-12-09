from django.contrib.auth.models import User
from django.db import models

class PhysicalAttributes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='physical_attributes')
    DOMINANT_HAND_CHOICES = [
        ("no-selection", "no-selection"),
        ("right", "Right"),
        ("left", "Left"),
        ("ambidextrous", "Ambidextrous"),
    ]

    EYE_COLOR_CHOICES = [
        ("no-selection", "no-selection"),
        ("brown", "Brown"),
        ("blue", "Blue"),
        ("green", "Green"),
        ("hazel", "Hazel"),
        ("gray", "Gray"),
        ("amber", "Amber"),
    ]

    HAIR_COLOR_CHOICES = [
        ("no-selection", "no-selection"),
        ("black", "Black"),
        ("brown", "Brown"),
        ("blonde", "Blonde"),
        ("red", "Red"),
        ("gray", "Gray"),
        ("white", "White"),
    ]

    height = models.PositiveIntegerField(help_text="Height in inches", null=True, blank=True)
    weight = models.PositiveIntegerField(help_text="Weight in lbs", null=True, blank=True)
    fastest_40_yard_dash = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Fastest 40-yard dash in seconds", null=True, blank=True
    )
    bench_press_max = models.PositiveIntegerField(help_text="Bench press max in lbs", null=True, blank=True)
    deadlift_max = models.PositiveIntegerField(help_text="Deadlift max in lbs", null=True, blank=True)
    squat_max = models.PositiveIntegerField(help_text="Squat max in lbs", null=True, blank=True)
    wingspan = models.PositiveIntegerField(help_text="Wingspan in inches", null=True, blank=True)
    vertical_jump_height = models.PositiveIntegerField(help_text="Vertical jump height in inches", null=True, blank=True)
    resting_heart_rate = models.PositiveIntegerField(help_text="Resting heart rate in bpm", null=True, blank=True)
    vo2_max = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, help_text="VO2 Max if known"
    )
    dominant_hand = models.CharField(
        max_length=12, choices=DOMINANT_HAND_CHOICES, default="right"
    )
    eye_color = models.CharField(max_length=12, choices=EYE_COLOR_CHOICES, default="brown")
    hair_color = models.CharField(max_length=12, choices=HAIR_COLOR_CHOICES, default="black")

    def __str__(self):
        return f"Attributes of ID {self.id}"
