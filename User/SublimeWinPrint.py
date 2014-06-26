import sublime
import sublime_plugin
import os, sys
import win32print


class SublimeWinPrint(sublime_plugin.TextCommand):

    def __init__(self, view):
        print view.fileName()

    def run(self, edit):
        self.printer = win32print.OpenPrinter(win32print.GetDefaultPrinter())
        print self.printer
