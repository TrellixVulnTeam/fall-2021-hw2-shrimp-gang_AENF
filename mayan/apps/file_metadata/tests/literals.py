from __future__ import unicode_literals

TEST_DRIVER_INTERNAL_NAME = 'exiftool'
TEST_FILE_METADATA_KEY = 'FileType'
TEST_FILE_METADATA_VALUE = 'PNG'
TEST_FILE_METADATA_INDEX_NODE_TEMPLATE = "{{{{ document.file_metadata_value_of.{}_{} }}}}".format(
    TEST_DRIVER_INTERNAL_NAME, TEST_FILE_METADATA_KEY
)
TEST_PDF_FILE_METADATA_DOTTED_NAME = 'exiftool.Producer'
TEST_PDF_FILE_METADATA_VALUE = 'pdfTeX-1.40.10'
