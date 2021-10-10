# apps/main/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.main.models import (
	CustomUser, AdminUser,
	StaffUser, MerchantUser,
	CustomerUser, Categories,
	SubCategories, Products,
	ProductMedia, ProductTransaction,
	ProductDetails, ProductAbout,
	ProductTags, ProductQuestions,
	ProductReviews, ProductReviewVoting,
	ProductVarient, ProductVarientItems,
	CustomerOrders, OrderDeliveryStatus,)

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AdminUser)
admin.site.register(StaffUser)
admin.site.register(MerchantUser)
admin.site.register(CustomerUser)
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(ProductMedia)
admin.site.register(ProductTransaction)
# admin.site.register(ProductDetails) # Error
# admin.site.register(ProductAbout) # Error
admin.site.register(ProductTags)
admin.site.register(ProductQuestions)
admin.site.register(ProductReviews)
admin.site.register(ProductReviewVoting)
admin.site.register(ProductVarient)
admin.site.register(ProductVarientItems)
admin.site.register(CustomerOrders)
admin.site.register(OrderDeliveryStatus)
