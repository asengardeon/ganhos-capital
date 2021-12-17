import json
import os
import subprocess
import sys
import unittest


class MyTestCase(unittest.TestCase):

    def __execute_cmd(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        return  out.decode("utf-8")


    def test_file_mode(self):
        result = self.__execute_cmd("python ../source/main.py --file resources/test_main_with_file.json")
        valid_values = json.loads(result)
        self.assertEqual(len(valid_values), 2)
        self.assertEqual(valid_values[0]['tax'], 0)
        self.assertEqual(valid_values[1]['tax'], 10000)

if __name__ == '__main__':
    unittest.main()
