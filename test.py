from unittest import TestCase
import staff
import user

class TestAccuracy(TestCase):
    def setUp(self) -> None:
        pass

    # def test_compute_hours(self):
    #     staffObj = staff()
    #     self.assertEqual(staffObj.computeHours("10:30:00","12:30:00"), 0)

    def test_check_username(self):
        userObj = user.user("Kenneth", "Araga", "kenneth15", "24", "meowmeow")
        self.assertIsNotNone(userObj.validateUsername(),None)
    
    def test_check_invalid_username(self):
        userObj = user.user("Kenneth", "Araga", "kennethsdsd15", "24", "meowmeow")
        self.assertEqual(userObj.validateUsername(),None)
    
    def test_display_username(self):
        userObj = user.user("Kenneth", "Araga", "kenneth15", "24", "meowmeow")
        self.assertEqual(userObj.printUserName(),"kenneth15")