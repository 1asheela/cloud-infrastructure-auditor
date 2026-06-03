from cli.commands import scan
def test_scan():
    result = scan()
    assert result is not None