from setuptools import setup, find_packages

setup(
    name='pypubsub',
    version='1.0.0',
    description='PyPubSub: basic inter-process communication implementation with publish-subscribe messaging pattern',
    author='Samy AB',
    author_email='dev@samyab.com',
    python_requires='~=3.9',
    extras_require={'dev': ['pytest', 'flake8']},
    packages=find_packages(exclude=['tests']),
)
