from dataclasses import dataclass

@dataclass
class Airport:
    iata_code: str
    name: str
    city: str
    state: str
    temperature: float
    delay: bool
