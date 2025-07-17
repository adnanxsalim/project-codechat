from setuptools import setup, find_packages

setup(
    name="codechat",
    version="1.0.0",
    description="AI CLI to analyze and refactor codebases",
    author="Adnan Salim",
    author_email="hello@adnansal.im",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "codechat=codechat.cli:main"
        ]
    },
    python_requires='>=3.8',
)
