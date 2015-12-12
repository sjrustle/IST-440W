# Shows system path
import unittest
import sys
sys.path.append('..')
import ConEng

class TestKerbAuthCheck(unittest.TestCase):
    def test_item_finder(self):
        con = ConEng.itemFinder("pillows",2)
        self.assertEqual(con,None)

    def test_error_compute(self):
        compute = ConEng.compute_error_for_line_give_points(1,1)
        self.assertTrue(compute)

    def test_step_grad(self):
        step = ConEng.step_gradient(1,1,2,.01)
        self.assertEqual(step,None)

    def test_run(self):
        run = ConEng.runtest('iPhone',2,360)
        self.assertTrue(run)





if __name__ == '__main__':
    unittest.main(exit = False)