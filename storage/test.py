from storage import Storage
from models import File
import time


store = Storage()

test = {
    "fname": "test.jpeg",
    "path":"/test/path/test.jpeg",
    "timestamp": time.time()
    }

new_file = store.save_file(test)



files = store.get_all()

print(files)