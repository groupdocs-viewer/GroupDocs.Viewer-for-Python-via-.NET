# This example demonstrates how to set a Metered license.

import aspose.groupdocsviewer as gv

def run():
    public_key = "*****"  # Your public key
    private_key = "*****"  # Your private key

    gv.Metered().set_metered_key(public_key, private_key)

    print("License set successfully.")

if __name__ == "__main__":
    run()
