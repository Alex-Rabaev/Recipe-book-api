from django.urls import path
from .views import RecipeCreateOrListAll, RecipeGetPutDelete, RecipeSearch

urlpatterns = [
    path("recipes", RecipeCreateOrListAll.as_view(), name="recipe-create-or-list-all"),
    path("recipes/<int:id>", RecipeGetPutDelete.as_view(), name="recipe-get-put-delete-by-id"),
    path("recipes/search", RecipeSearch.as_view(), name="recipe-search"),
]
