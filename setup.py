from setuptools import find_packages, setup

def get_requirements(file_path):
  requirements = []
  hypen_e_dot = "-e ."
  with open(file_path) as file_obj:
      requirements = file_obj.readlines()
      requirements = [req.replace("/n","") for req in requirements]

      if hypen_e_dot in requirements:
          requirements.remove(hypen_e_dot)
  return requirements
setup(
    name='ml_project1',
    version='0.1',
    description='Machine Learning Project',
    author='Kanak Vishwakarma',
    author_email='kanakvishwakarma000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("Requirements.txt"),
)