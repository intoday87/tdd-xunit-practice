class TestCase(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def setUp(self):
        self.wasSetup = 1


class WasRun(TestCase):
    def __init__(self, name):
       TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetup = 1

    def testMethod(self):
        self.wasRun = 1


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun('testMethod')

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetup(self):
        self.test.run()
        assert self.test.wasSetup

TestCaseTest('testRunning').run()
TestCaseTest('testSetup').run()
