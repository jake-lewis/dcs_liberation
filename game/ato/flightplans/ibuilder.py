from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.coalition import Coalition
    from game.data.doctrine import Doctrine
    from game.theater import ConflictTheater
    from game.threatzones import ThreatZones
    from ..flight import Flight
    from ..package import Package
    from .flightplan import Layout


class IBuilder(ABC):
    def __init__(self, flight: Flight, theater: ConflictTheater) -> None:
        self.flight = flight
        self.theater = theater

    @abstractmethod
    def build(self) -> Layout:
        ...

    @property
    def package(self) -> Package:
        return self.flight.package

    @property
    def coalition(self) -> Coalition:
        return self.flight.coalition

    @property
    def is_player(self) -> bool:
        return self.coalition.player

    @property
    def doctrine(self) -> Doctrine:
        return self.coalition.doctrine

    @property
    def threat_zones(self) -> ThreatZones:
        return self.coalition.opponent.threat_zone
