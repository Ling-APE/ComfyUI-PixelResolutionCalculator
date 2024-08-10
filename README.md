# ComfyUI-PixelResolutionCalculator

This node is used in the All-in-one Flux Dev workflow I made.

There is two node:
* PixelResolutionCalculator
* LatentSizeToPixelSize

The pixel resolution calculator is just a simple node that generate the closest "latent friendly" pixel resolution from your mega pixel and aspect ratio of choice. Took inspiration from the ImageScaleToTotalPixels node I saw from the original Flux demo workflow, since with flux everyone seems to talk about it with pixel resolution instead of width and height pixel count like SDXL. 

LatentSizeToPixelSize convert a laten samlpe input to width and height pixel count.
