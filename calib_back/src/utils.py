from src.settings import LEFT, RIGHT, ORIGINAL_FOLDER, PREVIEW_FOLDER, THUMBNAIL_FOLDER
from src.images import pair_exists

def check_for_error(side: str = "left", img_id: int = 0, img_type: str = "original"):
    error_msg = ""

    if not side in (LEFT, RIGHT):
        error_msg = f"{side} is an invalid side label, should be '{LEFT}' or '{RIGHT}'; "
    
    if not pair_exists(img_id):
        error_msg += f"Pair with id {img_id} doesn't exist; "

    if not img_type in (ORIGINAL_FOLDER, PREVIEW_FOLDER, THUMBNAIL_FOLDER):
        error_msg += f"{img_type} is an invalid image type; "
    
    return error_msg