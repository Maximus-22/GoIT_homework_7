from setuptools import setup, find_namespace_packages


setup(name = "clean_folder_mmv22",
    version = "1.0.1",
    description = "Sorting and transfer files in a specified folder",
    author = "maximus_22",
    author_email = "maksim.melnichenko@nservice.com.ua",
    readme = "README.md",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    license = "MIT",
    packages = find_namespace_packages(),
    entry_points = {"console_scripts":["run_cf = clean_folder_mmv22.run_clean_folder:run"] },
    install_requires = ["colorama", "requests"],
    )