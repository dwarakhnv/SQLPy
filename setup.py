from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="SQLPy",
    version="0.1.0",
    packages=find_packages(),
    # author="SQLPy",
    # author_email="SQLPy",
    # description="SQLPy",
    url='https://github.com/yourusername/SQLPy',  # Replace with your actual GitHub repo
    install_requires=[
        'pandas==2.2.3',
        'numpy==2.2.4',
        'pyodbc==5.2.0',
        'python-dateutil>=2.8.2'
    ],
    entry_points={
        "console_scripts": [
            # CLI Command = Module:Function
            # "sqlpy = SQLPy.__main__:main",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
)

