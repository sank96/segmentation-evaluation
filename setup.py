import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="segmentation-evaluation",
    version="1.0.3",
    scripts=['segmentation-evaluation'],
    author="Mattia Sanchioni, Alessandro Concetti",
    author_email="mattia.sanchioni.dev@gmail.com, ale.concetti@gmail.com",
    description="Segmentation evaluation tool",
    keywords="segmentation-evaluation segmentation evaluation image analysis image-analysis ground-truth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mett96/segmentation-evaluation",
    install_requires=['numpy',
                      'Shapely',
                      'opencv-contrib-python==3.4.2.17'],
    packages=setuptools.find_packages(),
    license="GPLv3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Scientific/Engineering :: Image Recognition"
    ],
    python_requires='>=3.6',
)