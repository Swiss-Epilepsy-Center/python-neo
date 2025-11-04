"""
Tests of neo.io.neomatlabio
"""

import unittest

from neo.io import MicromedIO
from neo.test.iotest.common_io_test import BaseTestIO


class TestMicromedIO(
    BaseTestIO,
    unittest.TestCase,
):
    ioclass = MicromedIO
    entities_to_download = ["micromed"]
    entities_to_test = ["micromed/File_micromed_1.TRC",
                        "micromed/File_micromed_24bit.TRC"]

    def test_micromed_24bit(self):
        filepath_24bit = self.get_local_path("micromed/File_micromed_24bit.TRC")
        reader = MicromedIO(filepath_24bit)
        segment = reader.read_segment()
        self.assertFalse((segment.analogsignals[0] > 10e5).any()) #An EEG-Signal above 10e5 uV is unrealistic

if __name__ == "__main__":
    unittest.main()
