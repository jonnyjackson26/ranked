from django.contrib.auth.models import User
from django.db import models

class PhysicalAttributes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='physical_attributes')
    DOMINANT_HAND_CHOICES = [
        ("right", "Right"),
        ("left", "Left"),
        ("ambidextrous", "Ambidextrous"),
    ]

    EYE_COLOR_CHOICES = [
        ("brown", "Brown"),
        ("blue", "Blue"),
        ("green", "Green"),
        ("hazel", "Hazel"),
        ("gray", "Gray"),
        ("amber", "Amber"),
    ]

    HAIR_COLOR_CHOICES = [
        ("black", "Black"),
        ("brown", "Brown"),
        ("blonde", "Blonde"),
        ("red", "Red"),
        ("gray", "Gray"),
        ("white", "White"),
    ]

    height = models.PositiveIntegerField(help_text="Height in inches")
    weight = models.PositiveIntegerField(help_text="Weight in lbs")
    fastest_40_yard_dash = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Fastest 40-yard dash in seconds"
    )
    bench_press_max = models.PositiveIntegerField(help_text="Bench press max in lbs")
    deadlift_max = models.PositiveIntegerField(help_text="Deadlift max in lbs")
    squat_max = models.PositiveIntegerField(help_text="Squat max in lbs")
    wingspan = models.PositiveIntegerField(help_text="Wingspan in inches")
    vertical_jump_height = models.PositiveIntegerField(help_text="Vertical jump height in inches")
    resting_heart_rate = models.PositiveIntegerField(help_text="Resting heart rate in bpm")
    vo2_max = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, help_text="VO2 Max if known"
    )
    dominant_hand = models.CharField(
        max_length=12, choices=DOMINANT_HAND_CHOICES, default="right"
    )
    eye_color = models.CharField(max_length=6, choices=EYE_COLOR_CHOICES, default="brown")
    hair_color = models.CharField(max_length=6, choices=HAIR_COLOR_CHOICES, default="black")

    def __str__(self):
        return f"Attributes of ID {self.id}"
