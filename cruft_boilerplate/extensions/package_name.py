"""Package name extension."""

__all__ = ["PackageNameExtension"]

import dataclasses

from jinja2 import Environment
from jinja2.ext import Extension


@dataclasses.dataclass
class PackageNameExtension(Extension):
    """Python package name jinja extension."""

    environment: Environment

    def __post_init__(self) -> None:
        """Post constructor."""

        def format_package_name(value: str) -> str:
            """Format python package name.

            :param value: the package name
            :return: the formatted package name
            """
            return value.replace("-", "_")

        self.environment.filters["package_name"] = format_package_name
