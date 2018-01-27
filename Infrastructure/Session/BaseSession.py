import os
import time
import hashlib

class BaseSession:
    session_id="__sessionId__"
    create_session_id = lambda: hashlib.sha1(bytes("%s%s" % (os.urandom(16),time.time()),encoding="utf-8")).hexdigest()