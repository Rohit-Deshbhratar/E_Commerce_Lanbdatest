import pytest


@pytest.mark.usefixtures("setup", "log_on_failure")
class BaseTest:
    pass
