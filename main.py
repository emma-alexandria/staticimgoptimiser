#!/usr/bin/python

import os
import filetype



def is_webp_file(filepath):
    kind = filetype.guess(filepath)
    if kind.MIME == "image/webp":
        return True
    else: 
        return False

def convert_to_webp(directory):
    for root, subdirs, files in os.walk(directory):
        for subdir in subdirs:
            subdir_path = os.path.join(root, subdir)
            for filename in os.listdir(subdir_path):
                if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                    input_path = os.path.join(subdir_path, filename)
                    if is_webp_file(input_path):
                        print(f"\033[33m [✓] {filename} is already a WebP image, skipping\033[0m")
                    else:
                        os.system(f'cwebp -q 80 "{input_path}" -o "{input_path}" -quiet')
                        print(f"\033[32m [✓] {filename} converted to WebP\033[0m")

# Example usage:
convert_to_webp('./static')