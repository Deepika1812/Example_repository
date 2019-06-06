import unittest
from TestLinkRunner import TestLinkRunner
class demonstratingTLRunner(unittest.TestCase):
    def test_11_TestPass(self):
        pass
    def test_4_TestPass(self):
        pass
    def test_15_TestPass(self):
        pass
    def test_19_TestPass(self):
        pass
    def test_21_TestPass(self):
        pass
    def test_25_TestPass(self):
        pass
    def test_31_TestPass(self):
        self.fail("test fail")
    def test_33_TestPass(self):
        pass
    def test_23_TestPass(self):
        self.fail("test fail")
testlinkURL = "http://localhost:8004/TestLink/lib/api/xmlrpc/v1/xmlrpc.php"
userKey = "4a975fb7ea42cdc39833c1504d3e4776"
suite = unittest.TestLoader().loadTestsFromTestCase(demonstratingTLRunner)
runner = TestLinkRunner(testlinkURL,userKey,_testPlanId=2,_buildName="MyFirstBuild")
runner.run(suite)
