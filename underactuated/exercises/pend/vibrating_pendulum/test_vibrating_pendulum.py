import unittest
import timeout_decorator
from gradescope_utils.autograder_utils.decorators import weight

class TestVibratingPendulum(unittest.TestCase):

    def __init__(self, test_name, notebook_locals):
        super().__init__(test_name)  # calling the super class init varies for different python versions.  This works for 2.7
        self.notebook_locals = notebook_locals

    @weight(8)
    @timeout_decorator.timeout(50.)
    def test_pendulum_controller(self):
        '''"Test pendulum controller"'''
        # note: all prints here go to the output item in the json file

        # the response must be monotonically increasing
        theta_dot = self.notebook_locals['logger'].data()[-1,:]
        self.assertTrue(
        	all(i <= j for i, j in zip(theta_dot, theta_dot[1:])),
        	msg='theta_dot(t) is decreasing.',
        	)

        # final theta dot in [.99, 1.001]
        self.assertLessEqual(
            theta_dot[-1],
            1.001,
            msg='theta_dot(t=10) = {} > 1.001'.format(theta_dot[-1]),
            )
        self.assertGreaterEqual(
            theta_dot[-1],
            .99,
            msg='theta_dot(t=10) = {} < 0.99'.format(theta_dot[-1]),
            )