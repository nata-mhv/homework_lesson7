import pytest
import os
import zipfile
from paths import TMP_DIR, ARC_DIR

@pytest.fixture(scope='session', autouse=True)
def archive_creation():
    if not os.path.exists('arc_dir'):
        os.mkdir('arc_dir')
        print('Created')
    with zipfile.ZipFile(os.path.join(ARC_DIR, 'file_zip.zip'), 'w') as zf:
        for file in os.listdir(TMP_DIR):
            zf.write(os.path.join(TMP_DIR, file), file)