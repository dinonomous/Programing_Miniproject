from django.shortcuts import render
from django.http import HttpRequest

def unit1(request):
    videos = [
        {"title": "* Series & Parallel Combinations of Resistance", "url": "https://www.youtube.com/embed/LyPJHijxWgk?autoplay=0&mute=1"},
        {"title": "* Source Transformation", "url": "https://www.youtube.com/embed/czkgGspvYF0?autoplay=0&mute=1"},
        {"title": "* Ohm's Law", "url": "https://www.youtube.com/embed/u5hx9L1ndaU?autoplay=0&mute=1"},
        {"title": "* Kirchhoffs Current Law (KCL)", "url": "https://www.youtube.com/embed/TaqJ4OYqv3A?autoplay=0&mute=1"},
        {"title": "* Kirchhoffs Voltage Law (KVL)", "url": "https://www.youtube.com/embed/aZIizOWnuB8?autoplay=0&mute=1"},
        {"title": "* Mesh Analysis", "url": "https://www.youtube.com/embed/xqmiQsbqplU?autoplay=0&mute=1"},
        {"title": "* SUPERPOSITION THEOREM", "url": "https://www.youtube.com/embed/ppIBGvdhVh4?autoplay=0&mute=1"},
        {"title": "* Thevenin Theorem", "url": "https://www.youtube.com/embed/WnAEB-JJda4?autoplay=0&mute=1"},
        {"title": "* Maximum Power Transfer", "url": "https://www.youtube.com/embed/SnESzDLFGAw?autoplay=0&mute=1"},
        {"title": "* Nodal Analysis", "url": "https://www.youtube.com/embed/wO3_vNhXf7A?autoplay=0&mute=1"},
        {"title": "* Star and Delta Connection", "url": "https://www.youtube.com/embed/-PuVmOLr5K8?autoplay=0&mute=1"},
        {"title": "* AC Circuit", "url": "https://www.youtube.com/embed/wH3_m8OKvVE?autoplay=0&mute=1"},
        {"title": "* AC Terminology Sums", "url": "https://www.youtube.com/embed/0UoeTIii1qY?autoplay=0&mute=1"},
        {"title": "* AC Average Value Sums", "url": "https://www.youtube.com/embed/gvzaQo4dlKc?autoplay=0&mute=1"},
        {"title": "* Peak, Average, MS Values Of Current & Voltage", "url": "https://www.youtube.com/embed/ckajfi4IpGs?autoplay=0&mute=1"},
        {"title": "* RMS Value Numericals", "url": "https://www.youtube.com/embed/6f1Mpz51dcY?autoplay=0&mute=1"},
    ]
    PDF = [
        
        {"name": "Material", "path": "https://drive.google.com/file/d/1ZTU9s3n6zktr44lhdUKiDnkyIXr1A5ZG/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Phy.html', context)
##################################################################################################################################

def unit2(request):
    videos = [
        {"title": "* Forward Bias (P N Junction Diode)", "url": "https://www.youtube.com/embed/icrAf1us2IQ?autoplay=0&mute=1"},
        {"title": "* Reverse Bias (P N Junction Diode)", "url": "https://www.youtube.com/embed/u_8b4GAUWCg?autoplay=0&mute=1"},
        {"title": "* Half Wave Rectifier", "url": "https://www.youtube.com/embed/gYxH-D9Det8?autoplay=0&mute=1"},
        {"title": "* Full Wave Rectifier", "url": "https://www.youtube.com/embed/8FAaLGxM98U?autoplay=0&mute=1"},
        {"title": "* Full Wave Bridge Rectifier", "url": "https://www.youtube.com/embed/OyENxMAVL_k?autoplay=0&mute=1"},
        {"title": "* Transistor Introduction (Bipolar Transistors & its Biasing)", "url": "https://www.youtube.com/embed/08jcU8rb9SU?autoplay=0&mute=1"},
        {"title": "* Operation of NPN Transistor", "url": "https://www.youtube.com/embed/tPE26DO3cDw?autoplay=0&mute=1"},
        {"title": "* CB configuration ", "url": "https://www.youtube.com/embed/RoN-sXrFXZI?autoplay=0&mute=1"},
        {"title": "* CE configuration", "url": "https://www.youtube.com/embed/bUx-9zu4syM?autoplay=0&mute=1"},
        {"title": "* CC configuration", "url": "https://www.youtube.com/embed/_ayby0owDWg?autoplay=0&mute=1"},
        {"title": "* FET (Field Effect Transistor) BJT Vs FET", "url": "https://www.youtube.com/embed/pd79hGW5ixI?autoplay=0&mute=1"},
        {"title": "* JFET (Junction Field Effect Transistor)", "url": "https://www.youtube.com/embed/5mimDymf0g0?autoplay=0&mute=1"},
        {"title": "* MOSFET", "url": "https://www.youtube.com/embed/X4_8dh-J4ik?autoplay=0&mute=1"},
        {"title": "* IGBT", "url": "https://www.youtube.com/embed/Bf7gzzykMcs?autoplay=0&mute=1"},
        {"title": "* SCR - Semiconductor Devices", "url": "https://www.youtube.com/embed/ShCJWYbHK64?autoplay=0&mute=1"},
        {"title": "* Types of Power Converter", "url": "https://www.youtube.com/embed/zkYyYlVYhQU?autoplay=0&mute=1"},
        {"title": "* Linear Voltage Regulators", "url": "https://www.youtube.com/embed/OAoEWaGtQjs?autoplay=0&mute=1"},
        {"title": "* SMPS", "url": "https://www.youtube.com/embed/Vo6gDr2F-Mw?autoplay=0&mute=1"},
        {"title": "* Karnaugh Map (K-map)", "url": "https://www.youtube.com/embed/lw1STgKUpW0?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Material", "path": "https://drive.google.com/file/d/1qjRs7SR6MVvj6Doh-rkUB7JPRDWN1Vev/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Phy.html', context)
###################################################################################################################################

def unit3(request):
    videos = [
        {"title": "* dc motor", "url": "https://www.youtube.com/embed/GwUikivkpK0?autoplay=0&mute=1"},
        {"title": "* construction of DC machine", "url": "https://www.youtube.com/embed/qXVAYN-OcfA?autoplay=0&mute=1"},
        {"title": "* single phase Transformer", "url": "https://www.youtube.com/embed/O96T1CfYlIo?autoplay=0&mute=1"},
        {"title": "* 3 phase AC induction motors", "url": "https://www.youtube.com/embed/59HBoIXzX_c?autoplay=0&mute=1"},
        {"title": "* Brushless DC Motor", "url": "https://www.youtube.com/embed/bCEiOnuODac?autoplay=0&mute=1"},
        {"title": "* SYNCHRONOUS MOTOR ", "url": "https://www.youtube.com/embed/Tk3lNBSAgEg?autoplay=0&mute=1"},
        {"title": "* Stepper Motor", "url": "https://www.youtube.com/embed/eyqwLiowZiU?autoplay=0&mute=1"},
        {"title": "* Servo Motor", "url": "https://www.youtube.com/embed/OYMJDFwVj-I?autoplay=0&mute=1"},
    ]
    PDF = [
        
        {"name": "Material", "path": "https://drive.google.com/file/d/1Tsuwsjv4mJzJUMrfNnZBV71aXypUbpxQ/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Phy.html', context)
###################################################################################################################################

def unit4(request):
    videos = [
        {"title": "* Deflecting, Controlling and Damping Torque", "url": "https://www.youtube.com/embed/FJzXhv9fihg?autoplay=0&mute=1"},
        {"title": "* Moving Iron Instruments", "url": "https://www.youtube.com/embed/K5JR1d3kpy8?autoplay=0&mute=1"},
        {"title": "*  PMMC Type Instruments ", "url": "https://www.youtube.com/embed/ZrjjnQw2dbs?autoplay=0&mute=1"},
        {"title": "* Digital Multimeter", "url": "https://www.youtube.com/embed/c5NeTnp_poA?autoplay=0&mute=1"},
        {"title": "* Digital Storage Oscilloscope DSO", "url": "https://www.youtube.com/embed/kUfJl0VDelk?autoplay=0&mute=1"},
        {"title": "* TRANSDUCERS|DEFINITION", "url": "https://www.youtube.com/embed/MiIeuxfTqo4?autoplay=0&mute=1"},
        {"title": "* CAPACITIVE TRANSDUCERS", "url": "https://www.youtube.com/embed/emtskVpbtyY?autoplay=0&mute=1"},
        {"title": "* Inductance Transducers", "url": "https://www.youtube.com/embed/N20lO9cWL9w?autoplay=0&mute=1"},
        {"title": "* LINEAR VARIABLE DIFFERENTIAL TRANSDUCER (LVDT)", "url": "https://www.youtube.com/embed/yriRrLivyaQ?autoplay=0&mute=1"},
        {"title": "* THERMISTOR", "url": "https://www.youtube.com/embed/sKU6NElYOKU?autoplay=0&mute=1"},
        {"title": "* Thermocouple TRANSDUCERS", "url": "https://www.youtube.com/embed/-hAicBabuvU?autoplay=0&mute=1"},
        {"title": "* PIEZOELECTRIC TRANSDUCERS", "url": "https://www.youtube.com/embed/E0NMM_Pq0IY?autoplay=0&mute=1"},
        {"title": "* HALL EFFECT TRANSDUCERS", "url": "https://www.youtube.com/embed/-GO-5YSGEfI?autoplay=0&mute=1"},
        {"title": "* PHOTOELECTRIC, Photodiodes, Phototransistors, Photoemissive TRANSDUCERS", "url": "https://www.youtube.com/embed/Dqx1RftB_P0?autoplay=0&mute=1"},
        {"title": "* LCD", "url": "https://www.youtube.com/embed/oNQTxWLYstk?autoplay=0&mute=1"},
        {"title": "* PROXIMITY SENSOR", "url": "https://www.youtube.com/embed/EQ4D9J---aQ?autoplay=0&mute=1"},
        {"title": "* IR Sensor", "url": "https://www.youtube.com/embed/zq51oZMzyP0?autoplay=0&mute=1"},
        {"title": "* Biosensors", "url": "https://www.youtube.com/embed/nxySi4rJkQE?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Material", "path": "https://drive.google.com/file/d/1h20bZ7ufTeEG852u4QO5uXhSGLMYzA_w/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Phy.html', context)
###################################################################################################################################

def unit5(request):
    videos = [
        {"title": "* Electrical Power Supply System", "url": "https://www.youtube.com/embed/CNVGvOr6RhA?autoplay=0&mute=1"},
        {"title": "* HVDC transmission system(monopolar, bipolar, homopolar)", "url": "https://www.youtube.com/embed/a-hjZSCgjvQ?autoplay=0&mute=1"},
        {"title": "* Indoor substation", "url": "https://www.youtube.com/embed/SaQ2wgwTjQk?autoplay=0&mute=1"},
        {"title": "* Earthing", "url": "https://www.youtube.com/embed/M5hP-EQ5GoM?autoplay=0&mute=1"},
        {"title": "* Pipe Earthing | Plate Earthing", "url": "https://www.youtube.com/embed/CzQcjKlsL7s?autoplay=0&mute=1"},
        {"title": "* hydrogen fuel cell", "url": "https://www.youtube.com/embed/GfJN3EMe0Jk?autoplay=0&mute=1"},
        {"title": "* BEV, PHEV, HEV", "url": "https://www.youtube.com/embed/qxmhFRx2fOw?autoplay=0&mute=1"},
    ]
    PDF = [
        
        {"name": "Material", "path": "https://drive.google.com/file/d/1_gnj3eoi9iSLFSgh2IL3kD90KBM-UQzm/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Phy.html', context)


# Create your views here.