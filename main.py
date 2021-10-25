# import the needed packages
import mintprocess
import stampdata
import tools


def main_function():
    # Wait 8 seconds so you are able to start the script,
    # switch to the browser
    # refresh the page with F5
    # and let the script do the job :)
    tools.wait(8)

    # load up the csv file and store the data into "stamp_data"
    stamp_data = stampdata.read_stamp_infos()

    # now start processing all entries from the csv
    for i in range(len(stamp_data)):
        # :) minty minty :)
        mintprocess.mint_process(stamp_data[i])


# call the main function to execute
main_function()
