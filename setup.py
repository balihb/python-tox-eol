from setuptools import setup, find_packages

setup(
    name='python-tox-eol',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=7.0',
        'pyyaml>=6.0'
    ],
    extras_require={
        'test': [
            'pytest>=6.2.5',
            'pytest-cov',
            'pytest-mock>=3.6.1'
        ]
    },
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pte=python-tox-eol.main:cli'
        ]
    }
)
