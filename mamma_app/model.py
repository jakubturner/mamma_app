from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Links(BaseModel):
    self: str


class Kilometers(BaseModel):
    estimated_diameter_min: float
    estimated_diameter_max: float


class Meters(BaseModel):
    estimated_diameter_min: float
    estimated_diameter_max: float


class Miles(BaseModel):
    estimated_diameter_min: float
    estimated_diameter_max: float


class Feet(BaseModel):
    estimated_diameter_min: float
    estimated_diameter_max: float


class EstimatedDiameter(BaseModel):
    kilometers: Kilometers
    meters: Meters
    miles: Miles
    feet: Feet


class RelativeVelocity(BaseModel):
    kilometers_per_second: str
    kilometers_per_hour: str
    miles_per_hour: str


class MissDistance(BaseModel):
    astronomical: str
    lunar: str
    kilometers: float
    miles: str


class CloseApproachDatum(BaseModel):
    close_approach_date: str
    close_approach_date_full: str
    epoch_date_close_approach: int
    relative_velocity: RelativeVelocity
    miss_distance: MissDistance
    orbiting_body: str


class EarthObject(BaseModel):
    links: Links
    id: str
    neo_reference_id: str
    name: str
    nasa_jpl_url: str
    absolute_magnitude_h: float
    estimated_diameter: EstimatedDiameter
    is_potentially_hazardous_asteroid: bool
    close_approach_data: List[CloseApproachDatum]
    is_sentry_object: bool


class EarthObjectParsed(BaseModel):
    name: str
    size_estimate: Kilometers
    time: str
    distance: float

    def __lt__(self, other: EarthObjectParsed) -> bool:
        return self.distance < other.distance

    def __le__(self, other: EarthObjectParsed) -> bool:
        return self.distance <= other.distance

    def __eq__(self, other: EarthObjectParsed) -> bool:
        return self.distance == other.distance

    def __ne__(self, other: EarthObjectParsed) -> bool:
        return self.distance != other.distance

    def __gt__(self, other: EarthObjectParsed) -> bool:
        return self.distance > other.distance

    def __ge__(self, other: EarthObjectParsed) -> bool:
        return self.distance >= other.distance
