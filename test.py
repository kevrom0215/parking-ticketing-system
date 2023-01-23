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

    def test_under_3_hours(self):
        timeObj = staff.computeHours("12:30:00","14:30:00")
        self.assertEqual(timeObj,50)

    def test_grace_period(self):
        timeObj = staff.computeHours("12:30:00","12:34:00")
        self.assertEqual(timeObj,0)

    def test_over_3_hours(self):
        timeObj = staff.computeHours("12:30:00","16:34:00")
        self.assertEqual(timeObj,60)

    def test_valid_plate(self):
        plateObj = staff.plateValidator("PVQ 373")
        self.assertIsNotNone(plateObj,None)

    def test_invalid_plate(self):
        plateObj = staff.plateValidator("nyeheh")
        self.assertEqual(plateObj,None)