workspace(name = "proto-bazel")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Python integration
rules_python_version = "0.1.0"
http_archive(
    name = "rules_python",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
    urls = [
        "http://github-cache.canva-build.com/bazelbuild/rules_python/releases/download/{version}/rules_python-{version}.tar.gz".format(version = rules_python_version),
        "https://github.com/bazelbuild/rules_python/releases/download/{version}/rules_python-{version}.tar.gz".format(version = rules_python_version),
    ],
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:pip.bzl", "pip_install")
pip_install(
    name = "foobar",
    requirements = "//examples/foobar/src:requirements.txt",
)






# mypy integration
# https://github.com/thundergolfer/bazel-mypy-integration/blob/master/README.md
mypy_integration_version = "0.1.0" # latest @ November 15th 2020

http_archive(
    name = "mypy_integration",
    sha256 = "511ca642294129b7abebf6afd48aa63e7d91de3ec5fa0689d60d1dc6a94a7d1a",
    strip_prefix = "bazel-mypy-integration-{version}".format(version = mypy_integration_version),
    url = "https://github.com/thundergolfer/bazel-mypy-integration/archive/{version}.tar.gz".format(
        version = mypy_integration_version,
    ),
)

load(
    "@mypy_integration//repositories:repositories.bzl",
    mypy_integration_repositories = "repositories",
)
mypy_integration_repositories()

load("@mypy_integration//:config.bzl", "mypy_configuration")
mypy_configuration("//tools/typing:mypy.ini")

load("@mypy_integration//repositories:deps.bzl", mypy_integration_deps = "deps")

mypy_integration_deps("//tools/typing:mypy_version.txt")

