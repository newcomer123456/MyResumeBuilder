from django.http import HttpResponseForbidden

class IsOwnerOrAdminMixin:
    """
    Міксина для перевірки, чи є користувач власником об'єкту або адміністратором.
    """
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()  # Отримуємо об'єкт, до якого звертається користувач
        if request.user.is_authenticated:
            if obj.user == request.user or request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden("Вам заборонено доступ до цього ресурсу.")
