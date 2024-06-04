from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recipe.models import Recipe
from .serializers import RecipeSerializer


class RecipeCreateOrListAll(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        if not recipes:
            return Response(
                {"message": "There are no recipes yet"}, status=status.HTTP_200_OK
            )
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecipeDetails(APIView):
    def get(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response(
                {"message": "The recipe doesn't exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response(
                {"message": "The recipe doesn't exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response(
                {"message": "The recipe doesn't exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        title = recipe.title
        recipe.delete()
        return Response(
            {
                "message": "The recipe has been deleted",
                "title": title,
            },
            status=status.HTTP_204_NO_CONTENT,
        )


class RecipeSearch(APIView):
    def get(self, request):
        query = request.query_params.get("q", "")
        recipes = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(
            category__icontains=query
        )
        if not recipes:
            return Response({"message": "No recipes found"}, status=status.HTTP_200_OK)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
