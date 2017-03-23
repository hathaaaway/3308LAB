#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Write a test to verify the constructor raises an error if passed something other than a string
    def test_constructor_error(self):
        with self.assertRaises(TypeError):
            textproc.Processor()

    # Write one or more unit tests to test the count() method
    def test_count(self):
        text = "four"
        p = textproc.Processor(text)
        self.assertEqual(4, p.count(), "Expected p.count() to return 4")

    # Write one or more unit tests to test the count_alpha() method
    def test_count_alpha(self):
        text = "F8o42Ur"
        p = textproc.Processor(text)
        self.assertEqual(4, p.count_alpha(), "Expected p.count_alpha() to return 4")

    # Write one or more unit tests to test the count_numeric() method
    def test_count_numeric(self):
        text = "135679F8o42Ur0"
        p = textproc.Processor(text)
        self.assertEqual(10, p.count_numeric(), "Expected p.count_numeric() to return 3")

    # Write one or more unit tests to test the count_vowels() method
    def test_count_vowels(self):
        text = "F8o42Urei"
        p = textproc.Processor(text)
        self.assertEqual(4, p.count_vowels(), "Expected p.count_vowels() to return 2")

    # Write one or more unit tests to test the is_phonenumber() method
    def test_is_phonenumber(self):
        goodNumber1 = textproc.Processor("303-345-3695")
        goodNumber2 = textproc.Processor("3033453695")
        goodNumber3 = textproc.Processor("(303) 345-3695")
        badNumber = textproc.Processor("s22-jsm-29sk")
        self.assertEqual(True, goodNumber1.is_phonenumber(), "expected '303-345-3695' to be valid phone number")
        self.assertEqual(True, goodNumber2.is_phonenumber(), "expected '3033453695' to be valid phone number")
        self.assertEqual(True, goodNumber3.is_phonenumber(), "expected '(303) 345-3695' to be valid phone number")
        self.assertEqual(False, badNumber.is_phonenumber(), "expected 's22-jsm-29sk' to NOT be valid phone number")

    # Find and correct any bugs the tests turn up

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
