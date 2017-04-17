from conans import ConanFile, CMake, tools
import os


class JanssonConan(ConanFile):
    name = "jansson"
    version = "2.10"
    license = "MIT"
    url = "https://jansson.readthedocs.io/"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    unzip_name = "jansson-{version}".format(version=version)
    zip_name = "{unzip_name}.tar.bz2".format(unzip_name=unzip_name)

    def source(self):
        tools.download("http://www.digip.org/jansson/releases/{zip_name}".format(zip_name=self.zip_name), self.zip_name)
        tools.unzip(self.zip_name)

    def build(self):
        self.run("cd {unzip_name} && ./configure && make".format(unzip_name=self.unzip_name))

    def package(self):
        self.copy("*.h", dst="include", src=self.unzip_name)
        self.copy("*.dll", dst="bin", src="{unzip_name}/src/.libs/".format(unzip_name=self.unzip_name))
        self.copy("*.so", dst="lib",  src="{unzip_name}/src/.libs/".format(unzip_name=self.unzip_name))
        self.copy("*.a", dst="lib", src="{unzip_name}/src/.libs/".format(unzip_name=self.unzip_name))
