from django.shortcuts import render
from django.http import HttpRequest

def unit1(request):
    videos = [
        {"title": "* Free electron theory", "url": "https://www.youtube.com/embed/v_lwiLkzavg?autoplay=0&mute=1"},
        {"title": "* Energy Band and Diagram", "url": "https://www.youtube.com/embed/k0_IcHt2z3w?autoplay=0&mute=1"},
        {"title": "* Differences | Conductor, Semiconductor, Insulator", "url": "https://www.youtube.com/embed/_GPhzPxWyQc?autoplay=0&mute=1"},
        {"title": "* Density of States", "url": "https://www.youtube.com/embed/_kijeUyE2S8?autoplay=0&mute=1"},
        {"title": "* Kronig Penney model", "url": "https://www.youtube.com/embed/ZoFOpJT_cN0?autoplay=0&mute=1"},
        {"title": "* E k diagram", "url": "https://www.youtube.com/embed/Jv3oV55tx7I?autoplay=0&mute=1"},
        {"title": "* Direct and Indirect Band Gap", "url": "https://www.youtube.com/embed/AI51R6_GRis?autoplay=0&mute=1"},
        {"title": "* Phonons (Short note)", "url": "https://www.youtube.com/embed/zBjak8lGTxY?autoplay=0&mute=1"},
        {"title": "* Fermi level Energy", "url": "https://www.youtube.com/embed/XCgCPWCN4qA?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Hand Writen Notes", "path": "https://drive.google.com/file/d/1Mz5crrUBjrRgCw2XfZGzDw6JGKpL-zGz/preview"},
        {"name": "Material", "path": "https://drive.google.com/file/d/1EpCP3eDKLddpEn2Jg5SmSmV1iKSeyBGS/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Scp.html', context)
##################################################################################################################################

def unit2(request):
    videos = [
        {"title": "* Intrinsic Semiconductor", "url": "https://www.youtube.com/embed/Yz_KfB1mj4Y?autoplay=0&mute=1"},
        {"title": "* Fermi Level energy in Intrinsic Semiconductor", "url": "https://www.youtube.com/embed/DK96DYQJTuI?autoplay=0&mute=1"},
        {"title": "* Extrinsic Semiconductor", "url": "https://www.youtube.com/embed/4PNiIsEDjSc?autoplay=0&mute=1"},
        {"title": "* N type Semiconductor", "url": "https://www.youtube.com/embed/dBhJ8TC94Ps?autoplay=0&mute=1"},
        {"title": "* P type Semiconductor", "url": "https://www.youtube.com/embed/jMOC-khmd1Y?autoplay=0&mute=1"},
        {"title": "* Intrinsic vs Extrinsic", "url": "https://www.youtube.com/embed/5WO24bCO9uo?autoplay=0&mute=1"},
        {"title": "* Drift and Diffusion Current", "url": "https://www.youtube.com/embed/GMH5rYbMkgs?autoplay=0&mute=1"},
        {"title": "* Continuity Equation", "url": "https://www.youtube.com/embed/cXnk-kE1Vy4?autoplay=0&mute=1"},
        {"title": "* PN junction", "url": "https://www.youtube.com/embed/-Ctm3pjOJ8k?autoplay=0&mute=1"},
        {"title": "* Forward bias and Reverse Bias", "url": "https://www.youtube.com/embed/_GCHMko6y_M?autoplay=0&mute=1"},
        {"title": "* Schottky Diode", "url": "https://www.youtube.com/embed/gh-3xWCTdbw?autoplay=0&mute=1"},
        {"title": "* Semiconductor materials used in Optoelectronic devices ", "url": "https://www.youtube.com/embed/XSvsf7Scb0o?autoplay=0&mute=1"},
        {"title": "* Light Emitting Diode (LED)", "url": "https://www.youtube.com/embed/lILf49pDeQc?autoplay=0&mute=1"},
        {"title": "* OLED (Organic Light Emitting Diode)", "url": "https://www.youtube.com/embed/AlAxPD3W4tc?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Material", "path": "https://drive.google.com/file/d/1sKKSW9jAM2ghsr2lhDJjYmsbVWInw4Dy/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Scp.html', context)
###################################################################################################################################

def unit3(request):
    videos = [
        {"title": "* Absorption of Radiation", "url": "https://www.youtube.com/embed/8vNs1b3NP8A?autoplay=0&mute=1"},
        {"title": "* Emission of Radiation (Spontaneous and Stimulated Emission)", "url": "https://www.youtube.com/embed/-y7Fzi_nYtc?autoplay=0&mute=1"},
        {"title": "* Optical Joint Density of States ", "url": "https://www.youtube.com/embed/YSx0GJBuURM?autoplay=0&mute=1"},
        {"title": "* Density of states photons", "url": "https://www.youtube.com/embed/Fd772_mTVnU?autoplay=0&mute=1"},
        {"title": "* Fermi Golden Rule", "url": "https://www.youtube.com/embed/u_CxPbCuUQg?autoplay=0&mute=1"},
        {"title": "* Photovoltaic Effect ", "url": "https://www.youtube.com/embed/qQYCsvX7jco?autoplay=0&mute=1"},
        {"title": "* Optical Loss (Causes & Remedy)", "url": "https://www.youtube.com/embed/Zno9Y5Oi1SM?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Hand Writen Notes", "path": "https://drive.google.com/file/d/1W6uRDIGqINmh8a2IvxicGt-FtHjU81EZ/preview"},
        {"name": "Material", "path": "https://drive.google.com/file/d/1unV63lasZsJM_pQarEDWeW9V1Fg93BuY/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Scp.html', context)
###################################################################################################################################

def unit4(request):
    videos = [
        {"title": "* Two Probe Method", "url": "https://www.youtube.com/embed/b28Kg0o2iT8?autoplay=0&mute=1"},
        {"title": "* Four Point Probe Method", "url": "https://www.youtube.com/embed/P-BYgUrTYzM?autoplay=0&mute=1"},
        {"title": "* Van Der Pauw Method ", "url": "https://www.youtube.com/embed/Zfw_nWA7aOY?autoplay=0&mute=1"},
        {"title": "* Hall Effect", "url": "https://www.youtube.com/embed/y0jSaUSCE8c?autoplay=0&mute=1"},
        {"title": "* Hot Point Probe", "url": "https://www.youtube.com/embed/hTFBn9gh0GA?autoplay=0&mute=1"},
        {"title": "* Capacitance Voltage Measurement (C-V Technique)", "url": "https://www.youtube.com/embed/IsuwnTadup4?autoplay=0&mute=1"},
        {"title": "* Boltzman Transport Equation", "url": "https://www.youtube.com/embed/uQ2NfAWjjoY?autoplay=0&mute=1"},
        {"title": "* Monte Carlo Methods", "url": "https://www.youtube.com/embed/feeYe0NRXVo?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Material", "path": "https://drive.google.com/file/d/109Q_Hf6-Bmailm5zGYLnEdVCcfIZHozm/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Scp.html', context)
###################################################################################################################################

def unit5(request):
    videos = [
        {"title": "* Density of States- 2D, 1D, 0D", "url": "https://www.youtube.com/embed/GKPsoXx_ZEw?autoplay=0&mute=1"},
        {"title": "* Carbon nanotubes", "url": "https://www.youtube.com/embed/DcAZCRLIZ2Q?autoplay=0&mute=1"},
        {"title": "* Physical Vapour Deposition Method", "url": "https://www.youtube.com/embed/V3BJ9cGMO9Y?autoplay=0&mute=1"},
        {"title": "* Chemical Vapour Deposition", "url": "https://www.youtube.com/embed/a_bR5xQ2xr8?autoplay=0&mute=1"},
        {"title": "* Transmission Electron Microscope (TEM)", "url": "https://www.youtube.com/embed/oLSiKHMRNu0?autoplay=0&mute=1"},
        {"title": "* Scanning Electron Microscope (SEM)", "url": "https://www.youtube.com/embed/FVMdog5zzE4?autoplay=0&mute=1"},
        {"title": "* Atomic Force Microscope (AFM)", "url": "https://www.youtube.com/embed/xnOqahYA6NU?autoplay=0&mute=1"},
    ]
    PDF = [
        {"name": "Hand Writen Notes", "path": "https://drive.google.com/file/d/1NBKvXFzRlqbUzdgQD554UAgxV1isQO8M/preview"},
        {"name": "Material", "path": "https://drive.google.com/file/d/1je6x4uK7VixF-AcXG6lvvdoCGtAC9YFW/preview"},
    ]

    # Pass the videos to the template
    context = {'videos': videos, 'PDF': PDF}

    # Render the HTML template with the data
    return render(request, 'Scp.html', context)


# Create your views here.