from common_libs import files

import download_default as dl


try:
    import download_custom as dl
except ImportError:
    pass


# Classes
#=======================================================================================================================
class AssetsDir(object):
    """
    Class to handle scrapper files
    """
    def __init__(self, pu_root):
        self._o_root = files.FilePath(pu_root)

    def box_dir(self, pu_platform):
        o_box_dir = files.FilePath(self._o_root.u_path, pu_platform, u'box')
        return o_box_dir

    def ingame_dir(self, pu_platform):
        o_ingame_dir = files.FilePath(self._o_root.u_path, pu_platform, u'ingame')
        return o_ingame_dir

    def title_dir(self, pu_platform):
        o_titles_dir = files.FilePath(self._o_root.u_path, pu_platform, u'title')
        return o_titles_dir


# Functions
#=======================================================================================================================
def download_images(po_dir, po_romdb_version):
    return dl.download_images(po_dir, po_romdb_version)


