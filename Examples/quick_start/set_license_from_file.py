import groupdocs.viewer as gv
import utils
import os
  

def run():
    if os.path.exists(utils.license_path):    
        license = gv.License()
        license.set_license(utils.license_path)
        print("License set successfully.")
    else:
       print("\n")


