import os
import json
import ssl
import urllib.request
from django.shortcuts import render
from .forms import WorkoutDataForm

def allowSelfSignedHttps(allowed):
    """Zaobilaženje SSL certifikata ako je potrebno (ako koristite self-signed certifikat)."""
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

def index(request):
    """Glavna funkcija za prikaz forme i rukovanje predviđanjem."""
    form = WorkoutDataForm(request.POST or None)
    prediction = None
    error = None

    if request.method == 'POST' and form.is_valid():  # Provjera da li je forma ispravno ispunjena
        try:
            # Dohvati podatke iz forme
            data = form.cleaned_data

            # Priprema podataka za slanje API-ju
            input_data = {
                "Inputs": {
                    "input1": [
                        {
                            "Age": data['age'],
                            "Gender": data['gender'],
                            "Weight (kg)": data['weight'],
                            "Height (m)": data['height'],
                            "Max_BPM": data['max_bpm'],
                            "Avg_BPM": data['avg_bpm'],
                            "Resting_BPM": data['resting_bpm'],
                            "Session_Duration (hours)": data['session_duration'],
                            "Workout_Type": data['workout_type'],
                            "Fat_Percentage": data['fat_percentage'],
                            "Water_Intake (liters)": data['water_intake'],
                            "Workout_Frequency (days/week)": data['workout_frequency'],
                            "Experience_Level": data['experience_level'],
                            "BMI": data['bmi']
                        }
                    ]
                },
                "GlobalParameters": {}
            }

            # Endpoint i API ključ
            url = 'http://1ec8fff8-9e36-4676-b417-c40e28848213.westeurope.azurecontainer.io/score'
            api_key = 'edW2xPXtvV52YyvwGPvMmQBdBeP4yzpn'

            # Priprema HTTP zahtjeva
            body = str.encode(json.dumps(input_data))
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            }

            req = urllib.request.Request(url, body, headers)
            response = urllib.request.urlopen(req)

            # Obrada odgovora s API-ja
            result = response.read()
            result = json.loads(result.decode("utf-8"))
            prediction = result['Results']['WebServiceOutput0'][0]['Predicted Calories']

        except Exception as e:
            # Ako dođe do greške prilikom slanja zahtjeva ili obrade odgovora
            error = str(e)

    return render(request, 'index.html', {'form': form, 'prediction': prediction, 'error': error})
