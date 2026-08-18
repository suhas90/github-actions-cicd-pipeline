from flask import jsonify


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify(
            {
                "application": "GitHub Actions CI/CD Demo",
                "status": "running",
                "version": "1.0.0",
            }
        )

    @app.route("/health")
    def health():
        return jsonify(
            {
                "status": "healthy"
            }
        )