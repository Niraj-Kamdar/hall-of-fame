"""Base class for storage."""

__author__ = 'Sergey Surkov'
__copyright__ = '2018 Sourcerer, Inc'


class StorageBase:
    def make_dirs(self, path):
        pass

    def move_file(self, from_path, to_path):
        pass

    def remove_file(self, path):
        pass

    def remove_subtree(self, path):
        pass

    def list_dir(self, dir_path, include_files=True, include_subdirs=True):
        pass

    def file_exists(self, file_path):
        pass

    def dir_exists(self, dir_path):
        pass

    def save_file(self, path, data, content_type='text/plain'):
        pass

    def load_file(self, path):
        pass
