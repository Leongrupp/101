from django.shortcuts import render


def index(request):
    """Render the main Telegram game page."""
    return render(request, "telegram_game/index.html")
