import shutil
import os

def pytest_sessionstart(session):
    archive_path = os.path.join(os.path.dirname(__file__), 'archive')
    shutil.rmtree(archive_path, ignore_errors=True)
    os.mkdir(archive_path)
