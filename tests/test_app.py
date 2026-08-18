from app import create_app


def test_home():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "GitHub Actions CI/CD Demo"
    assert data["status"] == "running"


def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"