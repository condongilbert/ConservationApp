# Conservation Efforts API

A simple Flask API to submit and retrieve conservation efforts.

## Features

- Submit a conservation effort (`/submit_effort`, POST)
- Retrieve all submitted efforts (`/get_efforts`, GET)
- Welcome message at root (`/`, GET)
- **Rate limiting** on submissions (via Flask-Limiter)

## Endpoints

...existing endpoint documentation...

## Rate Limiting

- Each IP is limited to 10 submissions per minute for effort submissions.
- The API has a default limit of 100 requests per hour per IP.
- If you exceed the limit, you'll receive a `429 Too Many Requests` error.

## Running the API

1. Install dependencies:
   ```sh
   pip install flask flask-limiter
   ```

2. Run the server:
   ```sh
   python conservation_api.py
   ```

3. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

...rest of your README...