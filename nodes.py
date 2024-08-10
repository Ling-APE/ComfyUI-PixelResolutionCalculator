import math
import torch

# Pixel Resolution Calculator

class PixelResolutionCalculator:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "megapixels": ("FLOAT", {"default": 2.0, "min": 0.1, "max": 100.0}),
                "aspect_ratio_width": ("INT", {"default": 3, "min": 1, "max": 100}),
                "aspect_ratio_height": ("INT", {"default": 4, "min": 1, "max": 100}),
                "divided_by": ("INT", {"default": 8, "min": 1, "max": 100}),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "calculate_resolution"
    CATEGORY = "image"

    def calculate_resolution(self, megapixels, aspect_ratio_width, aspect_ratio_height, divided_by):
        total_pixels = megapixels * 1e6
        gcd_value = math.gcd(aspect_ratio_width, aspect_ratio_height)
        width_ratio = aspect_ratio_width // gcd_value
        height_ratio = aspect_ratio_height // gcd_value
        multiplier = (total_pixels / (width_ratio * height_ratio)) ** 0.5
        width = int(width_ratio * multiplier)
        height = int(height_ratio * multiplier)

        # Round width and height to the nearest multiple of divided_by
        width = width - (width % divided_by)
        height = height - (height % divided_by)

        return width, height
    
# Latent Size to Pixel Size

class LatentSizeToPixelSize:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "samples": ("LATENT",),
                "latent_block_size": ("INT", {"default": 8, "min": 1, "max": 100})
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("pixel_width", "pixel_height")

    FUNCTION = "latent_to_pixel_size"
    CATEGORY = "image"

    def latent_to_pixel_size(self, samples, latent_block_size):
        size_dict = {}
        i = 0
        for tensor in samples['samples'][0]:
            if not isinstance(tensor, torch.Tensor):
                print("Error: Input should be a torch.Tensor")
                return None
            shape = tensor.shape
            tensor_height = shape[-2]
            tensor_width = shape[-1]
            size_dict.update({i:[tensor_width, tensor_height]})
        pixel_width = size_dict[0][0] * latent_block_size
        pixel_height = size_dict[0][1] * latent_block_size
        
        return (pixel_width, pixel_height)


