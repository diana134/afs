"""Creates any necessary directories and the database"""

import os
import errno

def make_sure_path_exists(path):
    """try to create the directories, show error if failure. Based on http://stackoverflow.com/questions/273192/check-if-a-directory-exists-and-create-it-if-necessary"""
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            print "Install failed with error: {0}".format(exception)
            print "Path: {0}".format(path)
            print "Please contact your administrator with the above details for assistance."

print "Creating directories..."
exportsPath = os.path.join("..", "Exports")
dbPath = os.path.join("..", "Database")
# TODO is this part necessary?
dbFilePath = os.path.join(dbPath, "AFS") 

make_sure_path_exists(exportsPath)
make_sure_path_exists(dbPath)
make_sure_path_exists(dbFilePath)

# TODO create db in here as well

print "Installation complete!"
