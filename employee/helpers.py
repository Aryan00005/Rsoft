import os
import uuid

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/uploads/<username>/<unique_id>.<extension>
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('uploads', instance.user.username, filename)