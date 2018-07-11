import os
import ycm_core

flags = [
    '-Wall',
    '-Wextra',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-DNDEBUG',
    '-std=c++11',
    '-stdlib=libstdc++',
    '-x', 'c++',
    '-I', 'src',
    '-I', 'include',
    '-isystem', '/usr/bin/../lib/gcc/x86_64-linux-gnu/7.2.0/../../../../include/c++/7.2.0',
    '-isystem', '/usr/bin/../lib/gcc/x86_64-linux-gnu/7.2.0/../../../../include/x86_64-linux-gnu/c++/7.2.0',
    '-isystem', '/usr/include/clang/4.0.1/include',
    '-isystem', '/usr/bin/../lib/gcc/x86_64-linux-gnu/7.2.0/../../../../include/c++/7.2.0/backward',
    '-isystem', '/usr/local/include',
    '-isystem', '/usr/include/x86_64-linux-gnu',
    '-isystem', '/usr/include',
    ]

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', ]

def FlagsForFile( filename, **kwargs ):
  return {
  'flags': flags,
  'do_cache': True
  }
