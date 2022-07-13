from setuptools import setup, find_packages

setup(
    name='python-tox-eol',
    version='1.0.0',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        'click>=7.0',
        'pyyaml>=6.0'
    ],
    extras_require={
        'test': [
            'pytest>=6.2.5',
            'pytest-cov'
        ]
    },
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pte=python_tox_eol.main:cli'
        ]
    }
)
