# File Service API

A Django REST API service that handles file management operations and provides random line retrieval functionality with multiple response format support.

## Features

- File Upload and Management
- Random Line Retrieval from Files
- Multiple Response Format Support (JSON, XML, Plain Text)
- Line Statistics (line number and most common letter)

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (Default Django Database)

## API Endpoints

### File Management
- `POST /upload/`: Upload new files.
- `GET /random-line/`: Get a Random line of a random uploaded file.
- `GET /random-line-backwards/`: Get a random line backwards from a random uploaded file.
- `GET /longest-20-lines/<file_name:str>/`: get the 20 longest lines in a specified file.
- `GET /longest-100-lines/`: get the 100 longest lines in all the files.

## Setup and Installation

1. Clone the repository
```bash
git clone <repository-url>
cd file_service
```
2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run migrations
```bash

python manage.py migrate
```
5. Start the development server
```bash
python manage.py runserver
```





