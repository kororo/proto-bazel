load("@rules_python//python:defs.bzl", "py_library", "py_test")
load("@foobar//:requirements.bzl", "requirement")
load("@mypy_integration//:mypy.bzl", "mypy_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "foobar",
    srcs = ["foobar.py"],
    deps = [
        requirement("boto3")
    ]
)

py_test(
    name = "foobar_test",
    size = "small",
    srcs = ["foobar_test.py"],
    tags = [
        "block-network",
        "unit",
    ],
    visibility = ["//visibility:private"],
    deps = [
        requirement("pytest"),
        ":foobar"
    ],
)

mypy_test(
    name = "foobar_mypy_test",
    deps = [
        ":foobar_test"
    ],
)