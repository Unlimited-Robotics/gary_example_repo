from setuptools import setup

package_name = 'gary_example_package'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/example_config.yaml']),
        ('share/' + package_name + '/launch', ['launch/example_launch.py']),  
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kai',
    maintainer_email='kai@unlimited-robotics.com',
    description='An example Python ROS 2 package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'example_engine = gary_example_package.example_engine:main',
        ],
    },
)
