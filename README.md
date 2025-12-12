[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "blackjack"
version = "0.0.2"
authors = [
    { name = "Dalton Shanholtz", email="dshanh01@rams.shepherd.edu" },
]
description = "A game of Blackjack - Final Project"
readme = "README.md"
requires-python = ">=3.8"
license = "ISC"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
dependencies = [
    "tkinter>8.6.12"
]

[project.urls]
Homepage = "https://github.com/daltons92/Final-Blackjack"
Issues = "https://github.com/daltons92/Final-Blackjack"
