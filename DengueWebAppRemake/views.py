from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def fault(request, fault):
    return render(request, 'fault.html', {'fault': fault})


def info(request):
    return render(request, 'info.html')


def view_info_page(request, uid):

    if uid == 1:
        return render(request, 'DosAndDonts.html')
    elif uid == 2:
        return render(request, 'faq.html')
    elif uid == 3:
        return render(request, 'aedesmosquito.html')
    elif uid == 4:
        return render(request, 'prevention.html')
    elif uid == 5:
        return render(request, 'signandsymptoms.html')
    elif uid == 6:
        return render(request, 'tests.html')
    elif uid == 7:
        return render(request, 'myths.html')
    elif uid == 8:
        return render(request, 'dryday.html')
    elif uid == 9:
        return render(request, 'message.html')
    elif uid == 10:
        return render(request, 'symptoms.html')


def map(request):
    return render(request, 'map.html')