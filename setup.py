# read the contents of your README file
from os import path

from setuptools import find_namespace_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "./README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="libero",
    version="0.1.0",
    description="LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone",
    author_email="bliu@cs.utexas.edu, yifengz@cs.utexas.edu",
    python_requires=">=3",
    # Treat top-level `libero` as a namespace package (PEP 420)
    packages=find_namespace_packages(include=["libero*"]),
    include_package_data=True,
    package_data={
        # Runtime assets (XMLs, textures, scenes, BDDL, etc.)
        "libero.libero": [
            "assets/**/*",
            "assets/**/*.*",
            "bddl_files/**/*",
            "bddl_files/**/*.*",
            "init_files/**/*",
            "init_files/**/*.*",
        ],
        # Configs are python modules; include to ensure availability when installed
        "libero.configs": ["**/*.py"],
        # Lifelong Python modules
        "libero.lifelong": ["**/*.py"],
    },
    install_requires=[],
    eager_resources=["*"],
    entry_points={
        "console_scripts": [
            "lifelong.main=libero.lifelong.main:main",
            "lifelong.eval=libero.lifelong.evaluate:main",
            # These two scripts live at submodules/libero/scripts/* and are not
            # part of the package; keep entry points for backward compat if present.
            "libero.config_copy=scripts.config_copy:main",
            "libero.create_template=scripts.create_template:main",
        ]
    },
)
