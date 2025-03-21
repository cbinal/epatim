from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from animal.models import Animal
from animal.api.serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]
    print("AnimalViewSet")

    def perform_create(self, serializer):
        # raise Exception("perform_create metodu çalıştı!")
        print(self.request.user)
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.id)
