from setuptools import setup, find_packages
import glob

setup(
    name = "cinrad",
    version = "1.0",
    description = "cinrad reading and plotting",
    long_description = "cinrad reading and plotting",
    license = "GPL Licence",
    author = "Du Puyuan",
    author_email = "dpy274555447@gmail.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "Windows",
    install_requires = [],
    data_files=[('cinrad', ['RadarStation.npy']),
                    ('cinrad\\colormap', glob.glob(r'colormap/*.txt')),
                    ('cinrad\\shapefile', glob.glob(r'shapefile/*'))],
    scripts = [],
    entry_points = {
        'console_scripts': [
            'test = test.help:main'
        ]
    }
)