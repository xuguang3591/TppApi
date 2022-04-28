import uuid

from App.settings import UPLOADS_DIR, FILE_PATH


def filename_transfer(filename):
    ext_name = filename.rsplit(".")[1]
    new_filename = uuid.uuid4().hex + "." + ext_name
    save_path = UPLOADS_DIR + new_filename
    upload_path = FILE_PATH + new_filename

    return save_path, upload_path