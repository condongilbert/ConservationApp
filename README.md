# Conservation Efforts API

A simple Flask API to submit and retrieve conservation efforts.

## Features

- Submit a conservation effort (`/submit_effort`, POST)
- Retrieve all submitted efforts (`/get_efforts`, GET)
- Welcome message at root (`/`, GET)

## Endpoints

### `POST /submit_effort`

Submit a new conservation effort.

**Request JSON:**
```json
{
  "user": "Your Name",
  "effort_type": "Type of Effort",
  "description": "Description of the effort"
}
```

**Response:**
- `200 OK` on success
- `400 Bad Request` if data is missing

### `GET /get_efforts`

Retrieve all submitted efforts.

**Response:**
- `200 OK` with a JSON array of efforts

### `GET /`

Returns a welcome message.

## Running the API

1. Install dependencies:
   ```sh
   pip install flask
   ```

2. Run the server:
   ```sh
   python conservation_api.py
   ```

3. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## File Structure

- `conservation_api.py`: Main Flask API source code.

## License