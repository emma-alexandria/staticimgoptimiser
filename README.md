# Staticimgoptimiser
Set a source dir, static dir, and valid extensions for source and image files. The script creates 4 sizes for srcset, and converts to webp.

## Process

1. Search through the static directory for non-webp image files matching the valid section. If specified, skip files in the root directory (e.g favicons). 
2. Create 4 distinct image sizes: 1x, 2x, 3x, and 4x. (4x being the original image size)
3. Convert each (including the original) to WebP at the specified compression level through [cwebp](https://developers.google.com/speed/webp/docs/cwebp) and resave them with their original file extension. The original serves as a fallback

## Limitations:

1. Will resize all images, even those of low resolution (e.g 100x100). This could lead to directory clutter
2. Cannot automatically determine the best size for the fallback image.
4. Ignores webp files for the purpose of determining what has and hasn't been compressed/processed before.

## Intended use: 

The intent of this script is to aid the process of content authoring - allowing one to put an image in the static directory without worrying about image optimisation (to an extent). In an ideal world, it would modify <img> tags - however this is complicated by intermediaries like MDSvex and components. For this reason my recommended (and personal) use is to create an image component which:
- Assumes the existence of the resized files
- Takes a path to the unresized image
- Uses the provided path in two fallbacks - one in `src` for browsers without support, and one in `onerror` in case the srcset images don't exist.

This allows you to write content as if you're just referencing the single image you imported, and have the optimisation handled automatically for you in your image component. I'd recommend putting this script in your run, build, and deploy scripts.


