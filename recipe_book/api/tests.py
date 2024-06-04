from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from recipe.models import Recipe


class RecipeTests(APITestCase):
    def setUp(self):
        self.recipe_data = {
            "title": "Spaghetti Carbonara",
            "description": "A classic Italian pasta dish with a creamy egg sauce.",
            "ingredients": [
                "200g spaghetti",
                "100g pancetta",
                "2 large eggs",
                "50g grated Parmesan cheese",
                "Salt",
                "Black pepper",
            ],
            "instructions": "...",
            "category": "Pasta",
        }
        self.invalid_recipe_data = {
            "title": "Spaghetti Carbonara",
            "description": "A classic Italian pasta dish with a creamy egg sauce.",
            "ingredients": "200g spaghetti",  # invalid format - should be list of strings
            "instructions": "...",
            "category": "Pasta",
        }
        self.recipe = Recipe.objects.create(**self.recipe_data)

    def test_create_recipe_success(self):
        url = reverse("recipe-create-or-list-all")
        response = self.client.post(url, self.recipe_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 2)
        self.assertEqual(response.data["title"], self.recipe_data["title"])

    def test_create_recipe_failure(self):
        url = reverse("recipe-create-or-list-all")
        response = self.client.post(url, self.invalid_recipe_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["ingredients"][0], "Ingredients must be a list.")
        self.assertEqual(Recipe.objects.count(), 1)

    def test_get_all_recipes(self):
        url = reverse("recipe-create-or-list-all")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_recipe_success(self):
        url = reverse("recipe-details-by-id", args=[self.recipe.id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.recipe.title)

    def test_get_single_recipe_failure(self):
        url = reverse("recipe-details-by-id", args=[999])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_recipe_success(self):
        url = reverse("recipe-details-by-id", args=[self.recipe.id])
        updated_data = {
            "title": "Updated Spaghetti Carbonara",
            "description": "An updated description.",
            "ingredients": [
                "250g spaghetti",
                "150g pancetta",
                "3 large eggs",
                "70g grated Parmesan cheese",
                "Salt",
                "Black pepper",
            ],
            "instructions": "Updated instructions...", # updated instructions
            "category": "Pasta",
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, updated_data["title"])
        self.assertEqual(self.recipe.instructions, updated_data["instructions"])

    def test_update_recipe_failure(self):
        url = reverse("recipe-details-by-id", args=[self.recipe.id])
        response = self.client.put(url, self.invalid_recipe_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_recipe_success(self):
        url = reverse("recipe-details-by-id", args=[self.recipe.id])
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Recipe.objects.count(), 0)

    def test_delete_recipe_failure(self):
        url = reverse("recipe-details-by-id", args=[self.recipe.id + 1])
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_recipes_found(self):
        url = reverse("recipe-search")
        response = self.client.get(url, {"q": "Spaghetti"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_recipes_not_found(self):
        url = reverse("recipe-search")
        response = self.client.get(url, {"q": "NonExistent"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "No recipes found")
