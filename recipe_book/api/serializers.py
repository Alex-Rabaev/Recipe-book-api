from rest_framework import serializers
from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "ingredients",
            "instructions",
            "category",
        ]

    def validate_ingredients(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Ingredients must be a list.")
        if not all(isinstance(item, str) for item in value):
            raise serializers.ValidationError("All ingredients must be strings.")
        return value

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.ingredients = validated_data.get("ingredients", instance.ingredients)
        instance.instructions = validated_data.get(
            "instructions", instance.instructions
        )
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance
