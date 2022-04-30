from lab6 import *
from lab6data import *
import unittest


class FunTestCase(unittest.TestCase):
    """Tests for methods of class Airpline"""

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up some stuff for [" + self.shortDescription() + "]")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after [" + self.shortDescription() + "]")

    def test_get_flight_id(self):
        """Test get flight id method"""
        Alltheflying= [Airline("AC3452", "Paris", "Ту134", '9.45', 'Wed'), Airline("SQ23", "London", "Airbus310", '12.20', 'Sat'), Airline("LH453", "Singapore", "SSJ100", '23.50', 'Wed'), Airline("AC3212", "Paris", "Boing747", '11.15', 'Fri'), Airline("SK421", "Zurich", "ИЛ86", '15.30', 'Wed')]        
        id=["AC3452", "SQ23","LH453", "AC3212", "SK421"]
        a=[]
        for i in range(len(Alltheflying)):
        	a.append(Alltheflying[i].get_flight_id())
        self.assertEqual(a,id)
        	
    def test_get_destination(self):
        """Test get destination method"""
        Alltheflying= [Airline("AC3452", "Paris", "Ту134", '9.45', 'Wed'), Airline("SQ23", "London", "Airbus310", '12.20', 'Sat'), Airline("LH453", "Singapore", "SSJ100", '23.50', 'Wed'), Airline("AC3212", "Paris", "Boing747", '11.15', 'Fri'), Airline("SK421", "Zurich", "ИЛ86", '15.30', 'Wed')]        
        d=["Paris","London","Singapore","Paris","Zurich"]
        a=[]
        for i in range(len(Alltheflying)):
        	a.append(Alltheflying[i].get_destination())
        self.assertEqual(a,d)

    def test_get_aircraft_type(self):
        """Test get aircraft type method"""
        Alltheflying= [Airline("AC3452", "Paris", "Ту134", '9.45', 'Wed'), Airline("SQ23", "London", "Airbus310", '12.20', 'Sat'), Airline("LH453", "Singapore", "SSJ100", '23.50', 'Wed'), Airline("AC3212", "Paris", "Boing747", '11.15', 'Fri'), Airline("SK421", "Zurich", "ИЛ86", '15.30', 'Wed')]        
        d=["Ту134","Airbus310","SSJ100","Boing747","ИЛ86"]
        a=[]
        for i in range(len(Alltheflying)):
        	a.append(Alltheflying[i].get_aircraft_type())
        self.assertEqual(a,d)

    def test_get_lead_time(self):
        """Test get lead time method"""
        Alltheflying= [Airline("AC3452", "Paris", "Ту134", '9.45', 'Wed'), Airline("SQ23", "London", "Airbus310", '12.20', 'Sat'), Airline("LH453", "Singapore", "SSJ100", '23.50', 'Wed'), Airline("AC3212", "Paris", "Boing747", '11.15', 'Fri'), Airline("SK421", "Zurich", "ИЛ86", '15.30', 'Wed')]        
        d=["9.45","12.20","23.50","11.15","15.30"]
        a=[]
        for i in range(len(Alltheflying)):
        	a.append(Alltheflying[i].get_lead_time())
        self.assertEqual(a,d)

    def test_get_days(self):
        """Test get days method"""
        Alltheflying= [Airline("AC3452", "Paris", "Ту134", '9.45', 'Wed'), Airline("SQ23", "London", "Airbus310", '12.20', 'Sat'), Airline("LH453", "Singapore", "SSJ100", '23.50', 'Wed'), Airline("AC3212", "Paris", "Boing747", '11.15', 'Fri'), Airline("SK421", "Zurich", "ИЛ86", '15.30', 'Wed')]        
        d=["Wed","Sat","Wed","Fri","Wed"]
        a=[]
        for i in range(len(Alltheflying)):
        	a.append(Alltheflying[i].get_days())
        self.assertEqual(a,d) 
		  	
		
if __name__ == '__main__':
    unittest.main()
