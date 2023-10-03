# serializers.py

from rest_framework import serializers

from .models import Book, Section, UserProfile


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

    def create(self, validated_data):
        user_role = validated_data.pop("user_role")
        if user_role == "Author":
            collaborators_data = validated_data.pop("collaborators", [])
            instance = Section.objects.create(**validated_data)
            for collaborator_data in collaborators_data:
                collaborator, created = UserProfile.objects.get_or_create(
                    **collaborator_data
                )
                instance.collaborators.add(collaborator)
        else:
            instance = None
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
