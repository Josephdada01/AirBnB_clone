#!/usr/bin/python3
""" Unittesting for console.py

Unittest classes:
    TestHBNBCommand_prompt
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand_prompt(unittest.TestCase):
    """Unittests for testing the prompt of the console"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_help(unittest.TestCase):
    """test for testing the help command"""
    def test_help_quit(self):
        h = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "===============================================\n"
             "EOF all create destroy help quit show update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """testing exiting functions in HBNB command interpreter"""
    def test_quit_exit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.asssertTrue(HBNBCommand().onecmd("EOF"))

class TestHBNBCommand_create(unittest.TestCase):
    """Testing the create function"""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        valid = "** class name missing **\n** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(valid, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        """ This will print unknown syntax and whatsoever the user type"""
        valid = "*** Unknown Syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(valid, output.getvalue().strip())

        valid = "*** Uknown syntax: BaseModel.create"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(valid, output.getvalue().strip())