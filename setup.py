import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lt2json-monvear",
    version="0.0.4",
    author="Moh. Novel Anugrah Ramdhani",
    author_email="moh.novelar@gmail.com",
    description="Convert log to json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohammadnovel/lt2json",
    project_urls={
        "Bug Tracker": "https://github.com/mohammadnovel/lt2json/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
	entry_points={
		"console_scripts": [
			'lt2json = lt2json.__main__:main'
		]
	},
)