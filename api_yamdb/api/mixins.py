from rest_framework import mixins, viewsets

"""ViewSet, который предоставляет действия по умолчанию `create()`, `destroy()` и `list()`."""
class ListCreateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass
