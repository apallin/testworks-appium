from setuptools import setup

__version__ = '0.1.0'
__url__ = 'https://github.com/apallin/testworks-appium/tarball/{}'.format(
    __version__)

setup(
    name='testworksappium',
    version=__version__,
    description="""
                A repository for Testworks Conf's Mobile Automation workshop
                presented by Adam Pallin
                """,
    author='Adam Pallin',
    author_email='adamrpallin@gmail.com',
    url='https://github.com/apallin/testworks-appium',
    packages=['testworksappium'],
    keywords=['appium', 'testworks'],
    download_url=__url__,
    install_requires=[
        'Appium-Python-Client >= 0.22, < 1.0',
    ],
)
