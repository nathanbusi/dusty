from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'dusty_slam'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),  # Install launch files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bambinojr',
    maintainer_email='nathan.busi00@gmail.com',
    description='SLAM package for Dusty',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
