from .nodes import PixelResolutionCalculator, LatentSizeToPixelSize  #import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

#__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

NODE_CLASS_MAPPINGS = {
    "PixelResolutionCalculator": PixelResolutionCalculator,
    "LatentSizeToPixelSize": LatentSizeToPixelSize,

}

NODE_DISPLAY_NAME_MAPPING = {
    "PixelResolutionCalculator": "Pixel Resolution Calculator",
    "LatentSizeToPixelSize": "Latent Size to Pixel Size"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]