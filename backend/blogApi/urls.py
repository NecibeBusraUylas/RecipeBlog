from django.urls import path, include
from .views import getAllCategoryApiView, getAllBlogApiView, getBlogByCategoryApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('blogs', getAllBlogApiView, basename='blogs')
router.register('categories', getAllCategoryApiView, basename='categories')
router.register('categoryBasedBlogs', getBlogByCategoryApiView, basename='categoryBasedBlogs')

urlpatterns = [
    path('', include(router.urls))
]