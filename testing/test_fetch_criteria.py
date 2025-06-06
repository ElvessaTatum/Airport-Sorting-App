import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.fetch_criteria import fetch_criteria, fetch_a_criterion
from src.sort_criteria.criteria_for_sort_name import criteria_for_sort as name_criterion
from src.sort_criteria.criteria_for_sort_city import criteria_for_sort as city_criterion
from src.sort_criteria.criteria_for_sort_city_and_name import criteria_for_sort as city_and_name_criterion

EXCEPTION_MESSAGE = "No criterion function found"

class FetchCriteriaTests(unittest.TestCase):
  def test_given_a_property_name_fetch_a_criterion_returns_the_appropriate_criteria_function(self):
    self.assertEqual(fetch_a_criterion("name"), name_criterion)

  def test_given_a_property_city_fetch_a_criterion_returns_the_appropriate_criteria_function(self):
    self.assertEqual(fetch_a_criterion("city"), city_criterion)

  def test_given_a_property_city_and_name_fetch_a_criterion_returns_the_appropriate_criteria_function(self):
    self.assertEqual(fetch_a_criterion("city and name"), city_and_name_criterion)

  def test_given_an_unfound_property_and_fetch_a_criterion_raises_an_exception(self):
    with self.assertRaises(Exception) as message: fetch_a_criterion("unfound property")
    self.assertEqual(str(message.exception), EXCEPTION_MESSAGE)

  def test_fetch_criteria_returns_a_list_that_contains_the_string_name(self):
    self.assertIn("name", fetch_criteria())

  def test_fetch_criteria_returns_a_list_that_contains_the_string_city_and_name(self):
    self.assertIn("city and name", fetch_criteria())

if __name__ == '__main__': 
  unittest.main()
