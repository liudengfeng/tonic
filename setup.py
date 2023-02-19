import setuptools


setuptools.setup(
    name="tonic",
    description="Tonic RL Library",
    url="https://github.com/fabiopardo/tonic",
    version="0.3.0",
    author="Fabio Pardo",
    author_email="f.pardo@imperial.ac.uk",
    packages=setuptools.find_packages(exclude=["data"]),
    install_requires=["gymnasium", "matplotlib", "numpy", "pandas", "pyyaml", "termcolor"],
    license="MIT",
    python_requires=">=3.6",
    keywords=["tonic", "deep learning", "reinforcement learning"],
)
