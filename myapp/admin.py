from django.contrib import admin
from .models import CustomUser, Blog, Business, Product, Farmer, CommunityPost, Comment, Reaction

# Custom User Admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'gender', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'gender')
    ordering = ('-date_joined',)

# Blog Admin
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'content')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

# Business Admin
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'contact')
    search_fields = ('business_name', 'contact', 'user__email')
    list_filter = ('user',)

# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'business', 'price', 'quantity_available')
    search_fields = ('product_name', 'business__business_name')
    list_filter = ('business',)

# Farmer Admin
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'user', 'quantity', 'contact')
    search_fields = ('product_name', 'user__email')
    list_filter = ('user',)

# Community Post Admin
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'content')
    search_fields = ('content', 'user__email')
    list_filter = ('created_at', 'user')

# Comment Admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at', 'content')
    search_fields = ('content', 'user__email', 'post__id')
    list_filter = ('created_at', 'user', 'post')

# Reaction Admin
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'reaction_type')
    search_fields = ('reaction_type', 'user__email', 'post__id')
    list_filter = ('reaction_type',)

# Register models in the admin interface
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Farmer, FarmerAdmin)
admin.site.register(CommunityPost, CommunityPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reaction, ReactionAdmin)
