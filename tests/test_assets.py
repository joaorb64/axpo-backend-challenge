from fastapi.testclient import TestClient
from app.main import app as main_app

client = TestClient(main_app)


def test_assets_endpoint():
    response = client.get("/assets")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:
        asset = data[0]
        assert "asset_id" in asset
        assert "signals" in asset
        assert isinstance(asset["signals"], list)

        if asset["signals"]:
            signal = asset["signals"][0]
            assert "signal_gid" in signal
            assert "signal_id" in signal
            assert "signal_name" in signal
            assert "asset_id" in signal
            assert "unit" in signal
