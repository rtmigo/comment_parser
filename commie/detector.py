import unittest
from pathlib import Path
from typing import Iterable

from . import *


def pickfunc(filename: str):
  filename = filename.lower()
  ext = filename.rpartition(".")[-1]

  if ext in ["c", "cpp", "java",
             "h", "hpp",
             # Objective-C source code 'implementation' program files usually
             # have .m filename extensions, while Objective-C 'header/interface' files
             # have .h extensions
             "m"]:
    return iter_comments_c

  if ext in ["go"]:
    return iter_comments_go

  if ext in ["js", "ts", "dart"]:
    return iter_comments_js

  if ext in ["html", "htm", "xml"]:
    return iter_comments_html

  if ext in ["rb"]:
    return iter_comments_ruby

  if ext in ["py"]:
    return iter_comments_python

  if ext in ["scss"]:
    return iter_comments_sass

  if ext in ["sh"]:
    return iter_comments_shell


class TestPickFunc(unittest.TestCase):
  def test_html(self):
    self.assertEqual(pickfunc(filename="file.html"), iter_comments_html)

  def test_js(self):
    self.assertEqual(pickfunc(filename="file.dart"), iter_comments_js)
    self.assertEqual(pickfunc(filename="file.js"), iter_comments_js)


def iter_comments(code: str, filename: str) -> Iterable[Comment]:
  func = pickfunc(filename)
  return func(code)

def iter_comments_file(file:Path) -> Iterable[Comment]:
  return iter_comments(file.read_text(), file.name)