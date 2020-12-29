import pytest

from unittest.mock import patch


@pytest.fixture(autouse=True)
@pytest.mark.asyncio
async def no_sleep():
    with patch("asyncio.sleep"), patch("time.sleep"):
        yield
