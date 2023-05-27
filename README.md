# Tester Tool for interactive problem

[![Releases](https://img.shields.io/github/v/release/SteGG200/tester_interactive)](https://github.com/SteGG200/tester_interactive/releases)
[![Build Status](https://app.travis-ci.com/SteGG200/tester_interactive.svg?branch=master)](https://github.com/SteGG200/tester_interactive)
[![platform](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/SteGG200/tester_interactive/releases)
[![Size](https://img.shields.io/github/repo-size/SteGG200/tester_interactive)](https://github.com/SteGG200/tester_interactive)
[![Python Version](https://img.shields.io/badge/python-%3E%3D%203.7-green)](https://www.python.org/downloads/)

Tester Tool is a command-line interface tool for using in interactive problem.

It's fast, useful, convenient

[Installation](#Installation) | [Usage](#Usage)

## Feature

- Communicate 2 executable or 2 program.

## Installation

You can download compiled binary file in [Here](https://github.com/SteGG200/tester_interactive/releases)

Then enjoy tester tool.

Or you can clone source code and compile it **(Python $\geq$ 3.7)**

```sh
$ git clone https://github.com/SteGG200/tester_interactive.git
$ cd tester_interactive
$ pyinstaller main.py --onefile --name=interactive
```

If you don't have `pyinstaller`, please use `pip install pyinstaller` before starting.

If you don't know `pyinstaller`, please see https://pyinstaller.org/en/stable/

After download, you should add tool to system environment variable `PATH`.

## Usage

Suppose you have a solution for an interactive problem, and you have a checker for it.

To communicate 2 program above, use this command: 

```sh
$ interactive checker.exe solution.exe
```

where `checker.exe` is your checker and `solution.exe` is you solution you want to check.

Set `solution.exe` run first (default `checker.exe` will run first):

```sh
$ interactive checker.exe solution.exe -f
```

Enter list of string that will end there communication (It always has empty string in list):

```sh
$ interactive checker.exe solution.exe -e a b c d
```

After running, tester will write all communication into `communication.log` file for you to see detail.
