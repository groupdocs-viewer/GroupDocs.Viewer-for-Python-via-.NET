from groupdocs.viewer import Metered

def set_metered_license():
    # Set your public and private keys
    public_key = "******" 
    private_key = "******" 

    # Check if keys are set
    if not public_key or public_key == "******" or not private_key or private_key == "******":
        print("Please set your public and private keys")
        return

    # Instantiate Metered and set keys
    metered = Metered()
    metered.set_metered_key(public_key, private_key)

    # Get a number of MBs processed 
    mb_processed = metered.get_consumption_quantity()
    print("MB processed: ", mb_processed)

    # Get a number of credits used
    credits_used = metered.get_consumption_credit()
    print("Credits used: ", credits_used)

if __name__ == "__main__":
    set_metered_license()