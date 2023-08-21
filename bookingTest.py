import unittest
from datetime import datetime
from collections import defaultdict

class TestBookingSystem(unittest.TestCase):

    def setUp(self):
        # Simulasi data dari Database
        self.bookings = [
            {"id": 1001, "venue_id": 15, "date": "2022-12-10", "start_time": "09:00:00", "end_time": "11:00:00", "price": 1200000},
            {"id": 1005, "venue_id": 15, "date": "2022-12-10", "start_time": "09:00:00", "end_time": "11:00:00", "price": 1000000}
        ]
        self.schedule = [
            {"id": 11, "venue_id": 15, "date": "2022-12-10", "start_time": "07:00:00", "end_time": "09:00:00", "price": 800000},
            {"id": 12, "venue_id": 15, "date": "2022-12-10", "start_time": "09:00:00", "end_time": "11:00:00", "price": 1000000},
            {"id": 13, "venue_id": 15, "date": "2022-12-10", "start_time": "11:00:00", "end_time": "13:00:00", "price": 1200000}
        ]

    def test_perbedaan_harga(self):
        for booking in self.bookings:
            for sched in self.schedule:
                if booking["date"] == sched["date"] and booking["start_time"] == sched["start_time"]:
                    self.assertEqual(booking["price"], sched["price"], f"Price discrepancy detected for booking id {booking['id']}")

    def test_double_booking(self):
        booking_counts = defaultdict(int)
        for booking in self.bookings:
            booking_counts[(booking["venue_id"], booking["date"], booking["start_time"], booking["end_time"])] += 1

        for count in booking_counts.values():
            self.assertEqual(count, 1, "Double booking detected")

if __name__ == "__main__":
    unittest.main()