from setuptools import setup, find_packages

setup(
    name="text-tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "text-tool=text_tool.cli:main",
        ],
    },
)