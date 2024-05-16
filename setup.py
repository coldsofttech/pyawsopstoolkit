from setuptools import setup, find_packages

import pyawsopstoolkit

setup(
    name=pyawsopstoolkit.__name__,
    version=pyawsopstoolkit.__version__,
    packages=find_packages(),
    url='https://github.com/coldsofttech/pyawsopstoolkit.git',
    license='MIT',
    author='coldsofttech',
    description=pyawsopstoolkit.__description__,
    requires_python=">=3.10",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[
        "aws", "toolkit", "operations", "tools", "development", "python", "validation", "session-management",
        "utilities", "enhancements", "integration", "amazon-web-services"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)
