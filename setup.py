import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="four-chan-ripper",
    version="0.0.3",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="Rips the contents of threads on 4chan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/four-chan-ripper",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/four-chan-ripper/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["four_chan_ripper"]),
    install_requires=['beautifulsoup4', 'lxml', 'prompt_toolkit', 'requests', 'rich', 'spawn-user-agent'],
    entry_points={
        'console_scripts': [
            '4cr = four_chan_ripper.__main__:_main'
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
