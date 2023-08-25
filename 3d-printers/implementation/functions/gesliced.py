"""
Move a print job to the folder GESLICED.
"""

import os
import sys

from directory_functions import (
    job_name_to_global_path,
    copy_print_job)
from cmd_farewell_handler import remove_directory_and_close_cmd_farewell
from create_batch_file import python_to_batch
from global_variables import FUNCTIONS_DIR_HOME

if __name__ == '__main__':

    job_name = sys.argv[1]
    job_global_path = job_name_to_global_path(job_name, search_in_main_folder='WACHTRIJ')

    gcode_files = [gcode_file for
                   gcode_file in os.listdir(job_global_path)
                   if gcode_file.lower().endswith('.gcode')]

    if len(gcode_files) == 0:
        print(f'warning! no .gcode files detected, slice .stl files first')
        sys.exit(0)

    # create the printer_aangezet.bat
    python_to_batch(os.path.join(FUNCTIONS_DIR_HOME, 'printer_aangezet.py'), job_name=job_name)

    copy_print_job(job_name, 'GESLICED', source_main_folder='WACHTRIJ')
    remove_directory_and_close_cmd_farewell()

