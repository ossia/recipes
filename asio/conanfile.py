import os

from conans import ConanFile, tools

def get_version():
    git = tools.Git()
    try:
        return "%s_%s" % (git.get_branch(), git.get_revision())
    except:
        return None
    
class AsioConan(ConanFile):    
    scm = {
       "type": "git",
       "subfolder": "asio",
       "url": "https://github.com/chriskohlhoff/asio",
       "revision": "531475f4"
    }
    name = "asio"
    version = "531475f4"
    no_copy_source = True
    
    def package(self):
       self.copy("asio/asio/include/*")
       
