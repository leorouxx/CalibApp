from collections import defaultdict

from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from src.settings import NO_CACHING, PREVIEW_FOLDER, ORIGINAL_FOLDER
from src.images import get_next_id, pair_exists, get_pair_names
from src.compute import generate_metadata, perform_calibration
from src.utils import check_for_error
from src.datatypes import ImageMetadata, SelectedPairs

### APP DEFINITION ###
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

### PERSISTENT DATA DEFINITION ###
IMAGE_METADATA: dict[int, dict[str, ImageMetadata]] = defaultdict(dict)

# id: {
#     left : {}
#     right: {}
# }

### ENDPOINTS DEFINITION ###

@app.get("/is_next_available/{previous_id}")
def is_next_available(previous_id: int):
    next_pair = get_next_id(previous_id)
    exitsts = pair_exists(next_pair)
    return {
        "exists": exitsts,
        "imgId": next_pair
    }    


@app.get("/get_image/{side}/{img_id}")
def get_image(side: str, img_id: int, type: str = PREVIEW_FOLDER): 
    #* rk : type isn't a nice name as it is a reserved keyword in python,
    #* but it is much more practical from the API pov
    
    side = side.lower()

    if (error_msg := check_for_error(side ,img_id, type)):
        return {
            "error": error_msg
        }

    names = get_pair_names(img_id, type)
    img_path = names[0] if side == "left" else names[1]

    return FileResponse(img_path, headers=NO_CACHING)


@app.get("/get_metadata/{side}/{img_id}")
def get_image_metadata(side: str, img_id: int):

    side = side.lower()
    if (error_msg := check_for_error(side ,img_id)):
        return {
            "error": error_msg,
        }
    
    # use cached metadata
    if IMAGE_METADATA[img_id].get(side, None) is not None: #valid expression thanks to defaultdict
        metadata = IMAGE_METADATA[img_id][side]
    
    # or compute them
    else:
        names = get_pair_names(img_id, ORIGINAL_FOLDER)
        img_path = names[0] if side == "left" else names[1]

        metadata = generate_metadata(img_path)

        IMAGE_METADATA[img_id][side] = metadata

    return {'id': img_id, 'side': side} | metadata


@app.post("/process_selected")
def process_selected(selected_pair: SelectedPairs):
    selected_ids = selected_pair.selectedIds

    if len(selected_ids) == 0:
        print("Error, no image to compute with")
        return

    metadata_subset = {
        k: v for k,v in IMAGE_METADATA.items() if k in selected_ids
    }

    results = perform_calibration(metadata_subset)

    return results

if __name__ == "__main__":
    from uvicorn import run

    run(
        "main:app",
        port=8000,
        reload=True,
    )