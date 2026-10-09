import os

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageSizeValidator:
    FILE_SIZE_LIMIT = 1048576

    def __init__(self, message):
        self.message = message


    def __call__(self, value):
        if value.size >= self.FILE_SIZE_LIMIT:
            raise ValidationError(self.message)


@deconstructible
class ImageTypeValidator:
    ALLOWED_IMAGE_TYPES = ['.jpg', '.jpeg', '.png']


    def __init__(self, message):
        self.message = message


    def __call__(self, value):
        if os.path.splitext(value.name)[1].lower() not in self.ALLOWED_IMAGE_TYPES:
            raise ValidationError(self.message)
