import unittest
import os

import HtmlTestRunner
import TestCaseFirst, TestCaseSecond

direct = os.getcwd()


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCaseFirst.GoogleSearch),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCaseSecond.LaunchFacebook),
        ])

       # outfile = open(direct + "./SmokeTest.html", "w")

        HtmlTestRunner.HTMLTestRunner(
          #  stream=outfile,
            report_title='Test Report',
            descriptions=True,
            combine_reports=True
        ).run(smoke_test)


if __name__ == '__main__':
    unittest.main(unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
            output='/home/rajesh/Documents/MCA/4Sem/STP/Automation/report-a')))