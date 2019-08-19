from datetime import datetime
from RAPIDpy.inflow import run_lsm_rapid_process
import os
#------------------------------------------------------------------------------
#main process
#------------------------------------------------------------------------------
if __name__ == "__main__":
    run_lsm_rapid_process(
        rapid_executable_location='/root/rapid/run/rapid',
        rapid_input_location=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'rapid_io_files')),
        lsm_data_location=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lsm_data')), #path to folder with LSM data
	rapid_output_location=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'streamflow')),
        use_all_processors=False, #defaults to use all processors available
        num_processors=1,#you can change this number if use_all_processors=False
    )
