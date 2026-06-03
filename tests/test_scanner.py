from cli.commands import scan
def test_scan():
    result = run_scan()
    assert result is not None