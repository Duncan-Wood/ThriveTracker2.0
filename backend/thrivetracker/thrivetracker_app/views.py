"""Views for the ThriveTracker2.0 app."""
from django.shortcuts import render

# Introuction Views
def introduction(request,):
    """A view that displays the introduction page"""
    return render(request, 'introduction/introduction.html', {})


def lets_start_personalizing(request,):
    """A view that displays the lets start personalizing page"""
    return render(request, 'introduction/lets-start-personalizing.html', {})


def weekly_drink_count(request):
    """A view that displays the weekly drink count page"""
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = "Monday"  # Replace with the actual current day
    count = 0  # Replace with the actual count

    context = {
        'days': days,
        'current_day': current_day,
        'count': count,
    }
    return render(request, 'introduction/weekly-drink-count.html', context)


def typical_week(request):
    """A view that displays the typical week page"""
    dry_days = 0  # Replace with the actual number of dry days
    drinks_per_week = 0  # Replace with the actual number of drinking days

    context = {
        'dry_days': dry_days,
        'drinks_per_week': drinks_per_week,
    }
    return render(request, 'introduction/typical-week.html', context)


def drink_recommendation(request):
    """A view that displays the drink recommendation page"""
    count = 21  # Replace with the actual count
    recommended_count = int(count * 0.85)

    context = {
        'count': count,
        'recommended_count': recommended_count,
    }
    return render(request, 'introduction/drink-recommendation.html', context)

# Daily Task Views