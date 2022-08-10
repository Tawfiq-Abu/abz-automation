import os
import glob
import sys
import pathlib


def run(app=None):
    path = pathlib.Path(__file__).parent.parent.resolve()

    if app:
        path = f"{path}/{app}/migrations/*.py"
    else:
        path = f"{path}/*/migrations/*.py"
        
    list_migration_files = glob.glob(path)
    for _file in list_migration_files:
        if not _file.endswith('__init__.py'):
            os.remove(_file)
    
    print('\nMigrations cleaned\n')
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run()