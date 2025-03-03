import os
import numpy as np

### FOLDER SETTINGS ###

IMAGE_FOLDER = "images"
ASSET_FOLDER = "assets"

ORIGINAL_FOLDER = "original"
PREVIEW_FOLDER = "preview"
THUMBNAIL_FOLDER = "thumbnail"

LEFT = "left"
RIGHT ="right"

IMG_NAME_TEMPLATE = "IMG_{}.JPG"

PLACEHOLDER = os.path.join(ASSET_FOLDER, "placeholder.jpg")

def get_image_path(side: str, img_id: int, img_type: str="original"):
    return os.path.join(IMAGE_FOLDER, side, img_type, IMG_NAME_TEMPLATE.format(img_id))

### IMAGE_SETTINGS ###
SCALE_FACTOR = {
    PREVIEW_FOLDER: 2,
    THUMBNAIL_FOLDER: 4,
}


### COMPUTATIONS ###

NUM_CORNERS = (9, 7)
N_POINTS = NUM_CORNERS[0] * NUM_CORNERS[1]

TILE_SIZE = 30  #in mm
HOR_DIST_CORNERS = (NUM_CORNERS[0] - 1) * TILE_SIZE
VER_DIST_CORNERS = (NUM_CORNERS[1] - 1) * TILE_SIZE

# creating a mesh grid
y = np.linspace(0, VER_DIST_CORNERS, NUM_CORNERS[1])
x = np.linspace(0, HOR_DIST_CORNERS, NUM_CORNERS[0])
[xx, yy] = np.meshgrid(x, y)
xx = xx.reshape(-1, 1)
yy = yy.reshape(-1, 1)
PTS_COORDS_Z = np.zeros((NUM_CORNERS[0] * NUM_CORNERS[1], 1), np.float32)
OBJ_PTS_COORDS = np.float32(np.hstack((xx, yy, PTS_COORDS_Z)))


### HTTP HEADERS ###

NO_CACHING = {
    "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
    "Pragma": "no-cache",
    "Expires": "0"
}