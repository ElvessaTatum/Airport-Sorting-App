import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.process_airports import process_airports
from src.airport import Airport
from src.sort_criteria.criteria_for_sort_iata import criteria_for_sort as sort_on_iata
from src.sort_criteria.criteria_for_sort_city import criteria_for_sort as sort_on_city
from src.sort_criteria.criteria_for_sort_name import criteria_for_sort as sort_on_name
from src.sort_criteria.criteria_for_sort_state import criteria_for_sort as sort_on_state
from src.sort_criteria.criteria_for_sort_temperature import criteria_for_sort as sort_on_temperature
from src.sort_criteria.criteria_for_sort_delay import criteria_for_sort as sort_on_delay
from src.sort_criteria.criteria_for_sort_city_and_name import criteria_for_sort as sort_on_city_and_name

class ProcessAirportsTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def setUp(self):
    self.iad = Airport("IAD", "DULLES INTL", "Washington", "DC", 71, True)
    self.ord = Airport("ORD", "O'HARE INTERNATIONAL", "Chicago", "IL", 62, True)
    self.mdw = Airport("MDW", "MIDWAY INTERNATIONAL", "Chicago", "IL", 60, False)

  def test_process_airports_takes_an_empty_list_and_returns_an_empty_list(self):
    self.assertEqual(process_airports([]), [])

  def test_process_airports_takes_one_airport_and_returns_that_airport(self):
    self.assertEqual(process_airports([self.iad]), [self.iad])

  def test_process_airports_takes_two_airport_and_returns_the_expected_result(self):
    expected_result = [self.iad, self.ord]

    self.assertEqual(process_airports([self.iad, self.ord]), expected_result)

  def test_process_airports_takes_three_airport_and_returns_the_expected_result(self):
    expected_result = [self.iad, self.ord, self.mdw]

    self.assertEqual(process_airports([self.iad, self.ord, self.mdw]), expected_result)

  def test_process_airports_takes_two_airports_and_returns_the_results_after_sorting_by_IATA_code(self):
    expected_result = [self.iad, self.ord]

    self.assertEqual(process_airports([self.ord, self.iad], sort_on_iata), expected_result)

  def test_process_airports_takes_three_airports_and_sorts_by_name(self):
    expected_result = [self.iad, self.mdw, self.ord]

    self.assertEqual(process_airports([self.iad, self.ord, self.mdw], sort_on_name), expected_result)

  def test_process_airports_takes_three_airports_and_sorts_by_city(self):
    expected_result = [self.ord, self.mdw, self.iad]

    self.assertEqual(process_airports([self.iad, self.ord, self.mdw], sort_on_city), expected_result)

  def test_process_airports_takes_three_airports_and_sorts_by_state(self):
    expected_result = [self.iad, self.ord, self.mdw]

    self.assertEqual(process_airports([self.iad, self.ord, self.mdw], sort_on_state), expected_result)

  def test_process_airports_takes_three_airports_and_sorts_by_temperature(self):
    expected_result = [self.mdw, self.ord, self.iad]

    self.assertEqual(process_airports([self.iad, self.ord, self.mdw], sort_on_temperature), expected_result)

  def test_process_airports_takes_three_airports_and_sorts_by_delay(self):
    expected_result = [self.mdw, self.iad, self.ord]

    self.assertEqual(process_airports([self.iad, self.ord, self.mdw], sort_on_delay), expected_result)

  def test_process_airports_takes_three_airports_and_sorts_by_city_and_name(self):
    expected_result = [self.mdw, self.ord, self.iad]

    self.assertEqual(process_airports([self.iad, self.ord, self.mdw], sort_on_city_and_name), expected_result)

  def test_process_airports_takes_an_airport_with_lowercase_name_and_the_returned_airport_has_name_in_uppercase(self):
    iah = Airport("IAH", "George Bush Intercont.", "Houston", "TX", 82, True)
    result = process_airports([iah])

    self.assertEqual(iah.name, "George Bush Intercont.")
    self.assertEqual(result[0].name, "GEORGE BUSH INTERCONT.")

if __name__ == '__main__': 
  unittest.main()
