from setuptools import setup, find_packages

setup(
    name="external_asset_mapper",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "pandas",
        "aiohttp"
    ],
    entry_points={
        "console_scripts": [
            "external_asset_mapper=external_asset_mapper.main:main"
        ]
    },
    author="Chris",
    description="A tool for mapping external assets via multiple validation sources.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
