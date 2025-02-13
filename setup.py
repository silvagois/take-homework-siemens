import os
from setuptools import find_packages, setup

setup(
    name="Log Analysis & Alerts",
    version=os.getenv("SERVICE_VERSION", "1.0.0"),
    description="Log Analysis and Alerting",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="Marcos Gois",
)
