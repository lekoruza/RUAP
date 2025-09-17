from django import forms

class WorkoutDataForm(forms.Form):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    WORKOUT_CHOICES = [('Yoga', 'Yoga'), ('HIIT', 'HIIT'), ('Cardio', 'Cardio'), ('Strength', 'Strength')]

    age = forms.IntegerField(label='Age', min_value=18, max_value=100)
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    weight = forms.FloatField(label='Weight (kg)', min_value=30.0, max_value=200.0)
    height = forms.FloatField(label='Height (m)', min_value=1.2, max_value=2.5)
    max_bpm = forms.IntegerField(label='Max BPM', min_value=40, max_value=300)
    avg_bpm = forms.IntegerField(label='Avg BPM', min_value=40, max_value=300)
    resting_bpm = forms.IntegerField(label='Resting BPM', min_value=40, max_value=300)
    session_duration = forms.FloatField(label='Session Duration (hours)', min_value=0.5, max_value=3.0)
    workout_type = forms.ChoiceField(label='Workout Type', choices=WORKOUT_CHOICES)
    fat_percentage = forms.FloatField(label='Fat Percentage', min_value=5.0, max_value=50.0)
    water_intake = forms.FloatField(label='Water Intake (liters)', min_value=1.0, max_value=5.0)
    workout_frequency = forms.IntegerField(label='Workout Frequency (days/week)', min_value=1, max_value=7)
    experience_level = forms.IntegerField(label='Experience Level', min_value=1, max_value=3)
    bmi = forms.FloatField(label='BMI', min_value=10.0, max_value=50.0)
