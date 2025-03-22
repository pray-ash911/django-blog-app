from django.apps import AppConfig  # Import AppConfig to configure the application

class BlogConfig(AppConfig):
    # Set the default type for auto-generated primary keys in models
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'  # ✅ Ensure the correct app name is here

    # This method is called when the application is fully loaded and ready
    def ready(self):
        # Import the signals module to ensure that signal handlers are registered
        import blog.signals  # Import signals to auto-create profiles and manage related data