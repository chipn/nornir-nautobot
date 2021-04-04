"""default network_importer driver for Ubiquiti EdgeRouter."""

from .default import NetmikoNautobotNornirDriver as DefaultNautobotNornirDriver


class NautobotNornirDriver(DefaultNautobotNornirDriver):
    """Collection of Nornir Tasks specific to Ubiquiti EdgeOS devices."""
