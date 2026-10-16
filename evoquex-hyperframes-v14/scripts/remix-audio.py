"""Legacy command compatibility: rebuild the NEW V14 composition only.

The rejected earlier backing stems are not loaded by this entry point.
"""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('compose-audio.py')),run_name='__main__')
