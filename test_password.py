# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_getEndOfLife(self):
        self.assertRaises(pwd.endofLifeException, pwd.getNext, 'zzzzz')

    def test_chaineVide(self):
        self.assertRaises(pwd.chaineVide, pwd.getNext, '')



# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
