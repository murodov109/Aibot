# Image Editing AI Service

class ImageEditingAI:
    def __init__(self, image_path):
        self.image_path = image_path

    def resize(self, width, height):
        """Resize the image to the given width and height."""
        pass  # Implementation here

    def apply_filter(self, filter_name):
        """Apply a filter to the image."""
        pass  # Implementation here

    def save(self, output_path):
        """Save the edited image to the specified path."""
        pass  # Implementation here

    def __str__(self):
        return f"ImageEditingAI(image_path={self.image_path})"