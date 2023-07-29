from setuptools import setup, find_packages


setup(
    name='gymnasium_connect_four',
    version='1.2.2',
    description='A connect 4 (connect four) environment for OpenAI Gym and Gymnasium',
    author='Lucas Bertola',
    url='https://github.com/lucasBertola/Connect-4-env',  
    # author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'pygame==2.1.3',
        'gymnasium==0.28.1',
    ]
)

#python setup.py sdist bdist_wheel
#twine upload dist/*