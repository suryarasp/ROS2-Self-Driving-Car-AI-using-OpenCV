from setuptools import setup
import os
from glob import glob


root_package = 'prius_sdc'
package_name = 'prius_sdc'
det_l_module ="prius_sdc/Detection/Lanes"
det_s_module ="prius_sdc/Detection/Signs"
config_module = "prius_sdc/config" 
data_module ="prius_sdc/data"
control_module ="prius_sdc/Control"
detec_l_a_module="prius_sdc/Detection/Lanes/a_Segmentation"
detec_l_b_module="prius_sdc/Detection/Lanes/b_Estimation"
detec_l_c_module="prius_sdc/Detection/Lanes/c_Cleaning"
detec_l_d_module="prius_sdc/Detection/Lanes/d_LaneInfo_Extraction"


    
setup(
    name=root_package,
    version='0.0.0',
    packages=[package_name,detec_l_d_module,detec_l_c_module,detec_l_b_module,config_module,det_l_module,det_s_module,data_module,control_module,detec_l_a_module],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + root_package]),
        ('share/' + root_package, ['package.xml']),
        (os.path.join('share', root_package), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='noshluk2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                    'sdc = prius_sdc.computer_vision_node:main',

        ],
    },
)
