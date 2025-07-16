# app.py
from api.v1 import create_app

app = create_app()

if __name__ == '__main__':
    # Use 0.0.0.0 for containerized deployments
    app.run(host='0.0.0.0', port=5000)
