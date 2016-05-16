# Github handle finder: Brute force Github for handles

import sys, os
import requests
from multiprocessing.pool import ThreadPool

def process_handle(h):
    base_url = "https://github.com/"
    if requests.get(base_url + h.rstrip()).status_code == 404:
    	return h
    return ""

def main(argv):
    # Check if arguments formed correctly
    if len(argv) < 1:
        sys.stderr.write("Usage: %s <dictionary>\n" % (argv[0],))
        return 1

    if not os.path.exists(argv[1]):
        sys.stderr.write("ERROR: Dictionary %r was not found!\n" % (argv[1],))
        return 1

    # Initiaize process variables
    handles = []

    # Iterate through the dictionary and save words into handles list
    print "Checking available Github handles..."
    with open(argv[1],'r') as dictionary:
    	for w in dictionary:
    		handles.append(w)

    # Process the handles in parallel
    print "Starting thread pool..."
    thread_pool = ThreadPool(100)
    valid_handles = thread_pool.map(process_handle, handles)

    # Remove duplicates from handles list
    valid_handles = sorted(list(set(valid_handles)))

    # Save results
    with open("results.txt", 'w') as out:
    	for h in valid_handles:
    		out.write(h)

    print "Done."

if __name__ == "__main__":
    sys.exit(main(sys.argv))
