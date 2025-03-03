import os

from src.settings import (
    get_image_path, 
    PLACEHOLDER, 
    ORIGINAL_FOLDER, 
    LEFT, 
    RIGHT, 
    SCALE_FACTOR
)
from src.compute import half_down_img

def get_next_id(prev_id: int) -> int:
    return prev_id + 1


def pair_exists(pair_id: int) -> bool:
    if pair_id == 0:
        return True

    r_path = get_image_path('left', pair_id)
    l_path = get_image_path('left', pair_id)

    return os.path.exists(r_path) and os.path.exists(l_path)


def ensure_file_existence(img_id: int, img_type: str):
    for side in (LEFT, RIGHT):
        modified_file = get_image_path(side, img_id, img_type)
        if os.path.exists(modified_file):
            continue
        
        original_file = get_image_path(side, img_id)
        half_down_img(SCALE_FACTOR[img_type], original_file, modified_file)



def get_pair_names(pair_id: int, img_type: str) -> tuple[str, str]:
    if pair_id == 0:
        return (PLACEHOLDER, PLACEHOLDER)

    if not pair_exists(pair_id):
        return ('', '')

    r_path = get_image_path('right', pair_id, img_type)
    l_path = get_image_path('left', pair_id, img_type)

    if img_type != ORIGINAL_FOLDER:
        ensure_file_existence(pair_id, img_type)

    return (l_path, r_path)