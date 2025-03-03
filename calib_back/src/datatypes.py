from pydantic import BaseModel

class Pair(BaseModel):
    id: int

class Point(BaseModel):
    x: float
    y: float

class ImageMetadata(BaseModel):
    foundCorners: bool
    corners : list[Point]

class SelectedPairs(BaseModel):
    selectedIds: list[int]