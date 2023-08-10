urlpatterns = [
    path('admin/', admin.site.urls),
+    path('hello/', views.hello_world),
]