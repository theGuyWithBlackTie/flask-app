from server import config
import os
from server.cache import Cache

MAX_FILE_SIZE      = 16 * 1024 * 1024
UPLOAD_FOLDER      = os.path.join(os.getcwd(), "storage")
ALLOWED_EXTENSIONS = set(['txt'])
SECRET_KEY         = "SDFOWPDKXVKDJFOS"
CACHE              = Cache(UPLOAD_FOLDER)