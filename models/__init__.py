#!/usr/bin/python3
""" 
import the Filestorage class 
from the file_storage file which is exist in engine package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
