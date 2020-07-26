import os

class Config:
    SECRET_KEY = os.environ['SECRET_KEY'] # or `os.urandom(32)` for single worker