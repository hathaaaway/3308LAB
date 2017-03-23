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

    # Add Your Test Cases Here...
    def test_count(self):
        string = "356adff&*&^lkio -s2"
        a = textproc.Processor(string)
        self.assertEqual(a.count(),19)

    def test_count_alpha(self):
        alpha = "abcd1234ABD"
        b = textproc.Processor(alpha)
        self.assertEqual(b.count_alpha(),4)

    def test_count_numeric(self):
        numeric = "12345abcdef"
        c = textproc.Processor(numeric)
        self.assertEqual(c.count_numeric(),5)

    def test_count_vowels(self):
        vowels = "aeioutuvmAE"
        d = textproc.Processor(vowels)
        self.assertEqual(d.count_vowels(),7)

    def test_is_phonenumber(self):
        phonenumber = "303-494-0341"
        e = textproc.Processor(phonenumber)
        self.assertTrue(e.is_phonenumber())

        phonenumber1 = "303 494 0341"
        f = textproc.Processor(phonenumber1)
        self.assertTrue(f.is_phonenumber())
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
