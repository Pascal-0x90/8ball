try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='eightball',
    version=0.1,
    description='Magic 8ball',
    author='Xc1d30us Mercy',
    author_email='',
    url='https://github.com/Xc1d30us-Mercy/8ball',
    packages=[
        'eightball'
    ],
    package_dir={'8ball': 'EightBall'},
    include_package_data=True,
    zip_safe=False,
    keywords='Magic EightBall'
)
