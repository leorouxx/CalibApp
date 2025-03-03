import numpy as np
import cv2

from src.settings import (
    LEFT, 
    RIGHT, 
    NUM_CORNERS, 
    N_POINTS, 
    OBJ_PTS_COORDS
)
from src.datatypes import ImageMetadata, Point

def half_down_img(reps: int, input_path: str, output_path: str) -> None:
    src = cv2.imread(input_path)
    for _ in range(reps):
        rows, cols, *_ = src.shape
        src = cv2.pyrDown(src, dstsize=(cols // 2, rows // 2))
    cv2.imwrite(output_path, src)


def find_corners(mask: np.ndarray, num_corners: tuple[int,int]) -> np.ndarray | None:
    """TODO: Flags to be adjusted"""

    # flags = cv2.CALIB_CB_NORMALIZE_IMAGE | cv2.CALIB_CB_EXHAUSTIVE
    # _, corners = cv2.findChessboardCornersSB(mask, num_corners, flags=flags)

    ret, corners = cv2.findChessboardCorners(mask, num_corners, None)
    
    if ret:
        return cv2.cornerSubPix(mask, corners, (11,11), (-1,-1), (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
    
    return None


def generate_metadata(img_path: str) -> ImageMetadata:
    '''
    Attempts to find corners of the chessboard.
    Parameters :
    ------------
        - img_path (str)
    
    Returns :
    ---------
        - (dict) : metadata dict
    '''
    img = cv2.imread(img_path)                                     
    corners = find_corners(img[..., 1], NUM_CORNERS)

    print(f"DEBUG in generate_metadata: {corners.shape=}")

    found = corners is not None and len(corners) == N_POINTS

    if isinstance(corners, np.ndarray):
        corners = corners.reshape((-1, 2))

        if (corners[0] < corners[-1]).all():                                                                                          
                  corners = corners[::-1]    

        corners= corners[::-1]
    else:
        corners = np.array([])

    return {
        'foundCorners' : found,
        'corners' : [
            {'x': float(point[0]), 'y': float(point[1])} for point in corners
        ] 
    }


def perform_calibration(img_metadata: dict[str, dict[str, ImageMetadata]]):
    INTRINSIC_FLAGS =  cv2.CALIB_FIX_K3# | cv2.CALIB_ZERO_TANGENT_DIST

    nb_pairs = len(img_metadata)
    objpoints = np.array([OBJ_PTS_COORDS]*nb_pairs)

    all_corners_l = []
    all_corners_r = []

    for metadatas in img_metadata.values():
        corners_l = metadatas[LEFT]['corners']
        corners_r = metadatas[RIGHT]['corners']

        all_corners_l.append(np.array([[corner['x'], corner['y']] for corner in corners_l]))
        all_corners_r.append(np.array([[corner['x'], corner['y']] for corner in corners_r]))




    ret_l, K_l, dist_l, rvecs_l, tvecs_l = cv2.calibrateCamera(objpoints, np.array(all_corners_l, dtype=np.float32), (6000, 4000), None, None, flags=INTRINSIC_FLAGS)
    ret_r, K_r, dist_r, rvecs_r, tvecs_r = cv2.calibrateCamera(objpoints, np.array(all_corners_r, dtype=np.float32), (6000, 4000), None, None, flags=INTRINSIC_FLAGS)
    
    print(
        f'{ret_l=}',
        f'{K_l=}',
        f'{dist_l=}',
        f'{rvecs_l=}',
        f'{tvecs_l=}',
        sep='\n'
    )

    print(
        f'{ret_r=}',
        f'{K_r=}',
        f'{dist_r=}',
        f'{rvecs_r=}',
        f'{tvecs_r=}',
        sep='\n'
    )