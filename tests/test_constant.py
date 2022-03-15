import pytest
import api.constant as constant



@pytest.marker.set1
async def test_constants():
    constants=constant.LANGUAGES
    assert constant == True


