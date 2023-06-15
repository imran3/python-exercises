import pytest
from src.safe_check import safe_check, safe_check_v2
from src.safe_check import SafeCheckResult

@pytest.mark.parametrize("input", ["This is safe", "But this is also safe", "what about this?"])
def test_safe_check_clean(input):
    res = safe_check(input)
    assert res == SafeCheckResult.CLEAN.value

@pytest.mark.parametrize("input", ["cute dog videos", "most funny meme of 2023", "Music genre of 70s", "can you keep a dog as pet?"])
def test_safe_check_banned(input):
    res = safe_check(input)
    assert res == SafeCheckResult.BANNED.value

@pytest.mark.parametrize("input", ["This is safe", "But this is also safe", "what about this?"])
def test_safe_check_v2_clean(input):
    res = safe_check_v2(input)
    assert res == SafeCheckResult.CLEAN.value

@pytest.mark.parametrize("input", ["cute dog videos", "most funny meme of 2023", "Music genre of 70s", "can you keep a dog as pet?"])
def test_safe_check_v2_banned(input):
    res = safe_check_v2(input)
    assert res == SafeCheckResult.BANNED.value