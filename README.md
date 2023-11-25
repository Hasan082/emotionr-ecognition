Certainly! Based on the information you provided, I'll try to create a more detailed structure for your project's `README.md`. Adjust it according to your project specifics.

```markdown
# Emotion Recognition Web App

This Django web application captures video from the user's camera, performs emotion recognition on detected faces, and displays the live video feed with detected emotions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Video Saving](#video-saving)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/emotion-recognition-app.git
cd emotion-recognition-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python manage.py runserver
```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Grant camera access.
3. Explore the live video feed with real-time emotion recognition.

## Features

- Real-time emotion recognition using OpenCV, DeepFace, and face-recognition.
- Displaying detected emotions as emojis.
- Live video feed with annotated faces.

## Video Saving

The application saves the live video feed with annotated emotions to `output.avi` in the project directory.

## Project Structure

```
emotionrecognition/
|-- emotionapp/
|   |-- migrations/
|   |-- static/
|   |-- templates/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- emotionrecognition/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- media/
|-- static/
|-- venv/
|-- .gitignore
|-- db.sqlite3
|-- manage.py
|-- README.md
|-- requirements.txt
|-- output.avi
```

Adjust the project structure section based on your actual project structure.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```