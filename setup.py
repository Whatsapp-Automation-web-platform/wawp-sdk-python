from setuptools import setup, find_packages

setup(
    name="wawp-sdk",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Wawp",
    author_email="support@wawp.net",
    description="Official Python Client for Wawp WhatsApp API. Modular, easy-to-use library for AI-powered WhatsApp automation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wawp-api/wawp-sdk-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
