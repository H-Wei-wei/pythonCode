
# 将某一文件夹中以某种命名规则的文件中所有的测试用例进行测试

import unittest

def createSuite():
    discovers = unittest.defaultTestLoader.discover("../src0807", pattern="BaiDu*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__=="__main__":
    discovers = createSuite()
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(discovers)
