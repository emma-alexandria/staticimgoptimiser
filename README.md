# staticimgoptimiser
Set a static dir, and valid extensions for source and image files. The script will create 4 sizes for srcset, and convert to webp.


## Notes
This was created for my personal site. It's barely tested - and for my own use. I just thought it might be useful to some people. 

**It was created and tested on a Linux machine.** If you want to use this on Windows, it'll need to be converted to support `\` pathfiles. If you make this change, I'd appreciate if you would submit it as a PR here. However, it's MIT licensed. I can't tell you what to do, I'm not your dad.

Also, it might summon Beezelbub and steal all your data or something. Again, very untested - use at your own risk.

## Details

### Process

1. Search through the static directory for non-webp image files with valid extensions. If specified, skip files in the root directory (e.g favicons). 
2. Convert each to webp (using [cwebp](https://developers.google.com/speed/webp/docs/cwebp)) at 4 distinct sizes (1x, 2x, 3x, 4x). 4x is the same as the original
3. Place these files in a `/processed` directory in the same dir as the original image

### Limitations:

1. Will resize all images, even those of low resolution (e.g 300x300). This could lead to unecessary directory clutter
2. Cannot automatically determine the best size for the fallback image (who can?)
3. Ignores webp files for the purpose of determining what has and hasn't been compressed/processed before.
4. No arguments - just edit the .py file
5. Existence of the resized files must be assumed in html. If the script breaks, your site won't build until it's fixed or you change the HTML.
6. Uses a naive webp compression setting. If your image is already kinda blasted, *it will look worse*.


### Intended use: 

The intent of this script is to aid the process of content authoring - allowing one to put an image in the static directory without worrying about image optimisation (to an extent). In an ideal world, it would modify <img> tags in your source - however this is complicated by intermediaries like MDSvex and components. For this reason my recommended (and personal) use is to create an image component which:
- Assumes the existence of the resized files
- Takes a path to the unresized image
- Uses the unresized path in two fallbacks - one in `src` for browsers without support, and one in `onerror` in case the srcset images don't exist.

This allows you to write content as if you're just referencing the single image you imported, and have the optimisation handled automatically for you in your image component. I'd recommend putting this script in your run, build, and deploy scripts.

## Requirements

- [filetype](https://pypi.org/project/filetype/)
- [cwebp](https://developers.google.com/speed/webp/docs/cwebp)

