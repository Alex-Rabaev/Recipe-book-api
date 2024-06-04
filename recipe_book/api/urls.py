from django.urls import path
from .views import RecipeCreateOrListAll, RecipeDetails, RecipeSearch

urlpatterns = [
    path("recipes", RecipeCreateOrListAll.as_view(), name="recipe-create-or-list-all"),
    path("recipes/<int:id>", RecipeDetails.as_view(), name="recipe-details-by-id"),
    path("recipes/search", RecipeSearch.as_view(), name="recipe-search"),
]
