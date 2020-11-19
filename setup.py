from setuptools import setup, find_packages
from datetime import datetime
from pathlib import Path


version = 0.1
with Path('README.md').open() as readme:
    readme = readme.read()


setup(
    name='gkd',
    version=version if isinstance(version, str) else str(version),
    keywords="LaTex", # keywords of your project that separated by comma ","
    description="Python tools for LaTex", # a concise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.7.0',
    url='https://github.com/thautwarm/gkd',
    author='thautwarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={"console_scripts": ["gkdmgr=gkd:callmain"]},
    install_requires=["paperbnf>=1.0"], # dependencies
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)


