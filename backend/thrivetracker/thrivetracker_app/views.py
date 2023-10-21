from django.shortcuts import render

def introduction(request,):
    return render(request, 'introduction/introduction.html', {})

def lets_start_personalizing(request,):
    return render(request, 'introduction/lets-start-personalizing.html', {})

def weekly_drink_count(request):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = "Monday"  # Replace with the actual current day
    count = 0  # Replace with the actual count

    context = {
        'days': days,
        'current_day': current_day,
        'count': count,
    }
    return render(request, 'introduction/weekly-drink-count.html', context)

def typical_week(request):
    dry_days = 0  # Replace with the actual number of dry days
    drinks_per_week = 0  # Replace with the actual number of drinking days

    context = {
        'dry_days': dry_days,
        'drinks_per_week': drinks_per_week,
    }
    return render(request, 'introduction/typical-week.html', context)
