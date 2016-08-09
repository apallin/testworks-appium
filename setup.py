from setuptools import setup

version = '0.1.0'
url = 'https://github.com/apallin/testworks-appium/tarball/{}'.format(version)

setup(
    name='testworksappium',
    version=version,
    description="""
                A repository for Testworks Conf's Appium Demo Presented
                by Adam Pallin
                """,
    author='Adam Pallin',
    author_email='adamrpallin@gmail.com',
    url='https://github.com/apallin/testworks-appium',
    packages=['testworksappium'],
    keywords=['appium', 'testworks'],
    download_url=url,
    install_requires=[
        'Appium-Python-Client >= 0.20, < 1.0',
        'requests >=2.5.1, <3.0',
    ],
)
