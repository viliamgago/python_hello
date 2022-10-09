import setuptools

setuptools.setup(
    name="python_hello",
    version="0.0.1",
    author="Cedd Burge",
    author_email="ceddlyburge@gmail.com",
    description="A function that returns 'hello world'",
    long_description_content_type="text/markdown",
    url="https://github.com/viliamgago/python-hello",
    packages=setuptools.find_packages(),
	install_requires=[
        'python_world@git+https://github.com/viliamgago/python_world#egg=python_world-0.0.1',
    ]
)