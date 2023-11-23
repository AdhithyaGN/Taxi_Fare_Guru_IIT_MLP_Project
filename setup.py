from setuptools import setup,find_packages
import os


def get_requirements(file)->list:
    requirement_list=[]
    with open(file,'r') as f:
        requirements=f.readlines()
        requirement_list=[r.replace('\n',"") for r in requirements]

    if "-e ." in requirement_list:
        requirement_list=requirement_list.remove('-e .')

    return requirement_list

setup(
    name='Taxi-Fare_Guru-Total_amount_Prediction',
    version='0.0.1',
    description='Total-amount-prediction using data from Taxi_Fare-guru as a part of kaggle competition',
    author='Adhithya G Nair',
    author_email='adhithyagnair97@gmail.com',
    url='https://github.com/AdhithyaGN/Taxi_Fare_Guru_IIT_MLP_Project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)









