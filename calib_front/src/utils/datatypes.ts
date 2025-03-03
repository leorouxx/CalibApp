export type Side = 'left' | 'right'

export type Point = {
    x: number;
    y: number;
}

export type Pair = {
    id: number;
    selected: boolean;
}

export type Existence = {
    exists: boolean;
    imgId: number;
}

export type Metadata = {
    id: number;
    side: Side;
    foundCorners: boolean;
    corners: Array<Point>;
}