"""
lasdata: LAS data reader, writer, and converter

This module provides functionality to handle LAS (Log ASCII Standard) files 
in formats 1.0, 1.1, 1.2, 1.3, and 1.4, supporting point formats 0-10. It 
is designed for quick manual loading, editing, repairing, and saving of 
LAS files.

Features:
- Load LAS files using `LasData('file.las')`.
- By default, loads only XYZ coordinates. Additional data can be accessed 
  using `get_<variable_name>()` methods.
- Users are free to modify class member variables, though the tool makes 
  minimal checks for data integrity.

Output:
- Data is saved in the format specified in the class header. Alternatively, 
  the `write_las` method can be used to specify a target format during saving.

Note:
This tool is intended for manual LAS file manipulation. Use responsibly to 
avoid accidental data corruption.

Original MATLAB version by Teemu Kumpumki, Tampere University of Technology, 2014.
Python rewrite with equivalent functionality and additional improvements.
"""

import numpy as np
import laspy

class LasData(object):
    def __init__(self, filename: str):
        # Read in .las file
        LiDAR_data = laspy.read(filename)

        


