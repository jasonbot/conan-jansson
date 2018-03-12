from conans import ConanFile
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
        shared = 'yes' if self.options.shared else 'no'
        self.run("cd {unzip_name} && ./configure --enable-shared={shared} && make".format(unzip_name=self.unzip_name, shared=shared))

    def package(self):
        self.copy("*.h", dst="include", src=self.unzip_name, keep_path=False)
        self.copy("*.dll", dst="bin", src="{unzip_name}/src/.libs/".format(unzip_name=self.unzip_name))
        self.copy("*.so", dst="lib",  src="{unzip_name}/src/.libs/".format(unzip_name=self.unzip_name))
        self.copy("*.a", dst="lib", src="{unzip_name}/src/.libs/".format(unzip_name=self.unzip_name))

    def package_info(self):
        self.cpp_info.libs = ['jansson']
