from setuptools import setup, find_packages

setup(
    name='FinamPy',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests', 'pandas', 'numpy'],  # Укажите зависимости, если они известны
)