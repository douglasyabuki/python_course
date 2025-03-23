# PySide6 for GUI (Graphical User Interface) using Qt in Python - Installation
# - The original section of this course used PyQt5 (now updated to PySide6).
# - Both libraries (PySide and PyQt) use the Qt framework.
# - Qt is a library used to create GUIs, originally written in C++.
#   - PySide and PyQt provide bindings between Python and the Qt framework,
#     allowing GUI creation without using another programming language.
# - PySide6 refers to version 6 of Qt (Qt 6).
# - Qt is cross-platform, meaning it runs on Windows, Linux, and macOS.

# Why did we switch from PyQt to PySide in this update?
# - PySide was developed by The Qt Company (from Nokia), as part of
#   the "Qt for Python" project: https://doc.qt.io/qtforpython/
# - Since PySide and PyQt both use Qt, they are extremely similar,
#   often the code is identical. Thus, if you still want to use PyQt,
#   porting the code will be simple—often just switching between PySide and PyQt.
# - The main difference between PyQt and PySide is the license:
#   PyQt uses GPL or a commercial license, while PySide uses LGPL.
#   In short, with PySide you can use the library commercially without
#   having to release your source code publicly.
#   Licenses are complex topics, so make sure you fully understand them
#   before using any third-party software:
#   https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)

import PySide6.QtCore

# Print the PySide6 library version
print(PySide6.__version__)  # type: ignore

# Print the version of Qt used by PySide6
print(PySide6.QtCore.__version__)  # type: ignore
