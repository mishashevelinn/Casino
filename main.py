import cx_Freeze

import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("App.py", base=base, icon="bg1.ico")]

cx_Freeze.setup(
    name="Misha's-Client",
    options={"build_exe": {"packages": ["tkinter", "matplotlib"], "include_files": ["bg1.ico", "bg.png"]}},
    version="0.01",
    description="Casino Forecast",
    executables=executables
)
