from django.http import JsonResponse


class BlockBrowserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get("HTTP_USER_AGENT", "").lower()
        if "mozilla" in user_agent or "chrome" in user_agent:
            return JsonResponse({"error": "API tarayıcıdan erişilemez."}, status=403)
        return self.get_response(request)
