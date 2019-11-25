from glob import glob
import os

import pkg_resources

from .__about__ import __version__


def patches():
    all_patches = {}
    for path in glob(
        os.path.join(pkg_resources.resource_filename("tutorenableLTI", "patches"), "*")
    ):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
