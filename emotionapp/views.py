from django.conf import settings
from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
from deepface import DeepFace
import face_recognition
import time
import emoji

DURATION = 5


def map_to_emoji(emotion):
    emoji_mapping = {
        "Happiness": emoji.emojize(":smile:"),
        "Sadness": emoji.emojize(":cry:"),
        "Anger": emoji.emojize(":angry:"),
        "Fear": emoji.emojize(":scream:"),
        "Disgust": emoji.emojize(":nauseated_face:"),
        "Surprise": emoji.emojize(":open_mouth:"),
        "Neutral": emoji.emojize(":neutral_face:")
    }
    return emoji_mapping.get(emotion, emoji.emojize(":question:"))


def map_to_basic_emotion(emotion):
    basic_emotions = {
        "happy": "Happiness",
        "sad":   "Sadness",
        "angry": "Anger",
        "fear":  "Fear",
        "disgust": "Disgust",
        "surprise": "Surprise",
        "neutral": "Neutral"
    }
    return basic_emotions.get(emotion, "Unknown")


def process_frame(frame):
    face_locations = face_recognition.face_locations(frame)
    results = []

    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]
        predictions = DeepFace.analyze(face_image, actions=['emotion'],
                                       enforce_detection=False)

        if isinstance(predictions, dict):
            raw_emotion = predictions.get('dominant_emotion', 'Unknown')
        elif isinstance(predictions, list) and len(predictions) > 0:
            raw_emotion = predictions[0].get('dominant_emotion', 'Unknown')
        else:
            raw_emotion = "Unknown"

        basic_emotion = map_to_basic_emotion(raw_emotion)
        emo = map_to_emoji(basic_emotion)

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        results.append((timestamp, basic_emotion, emo))

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, basic_emotion, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    return frame, results


def generate_frames():
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter(settings.VIDEO_OUTPUT_PATH, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
    start_time = time.time()
    results = []

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > DURATION:
            break

        ret, frame = cap.read()
        if not ret:
            break

        frame, frame_results = process_frame(frame)
        results.extend(frame_results)

        # Write the frame to the video file
        out.write(frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    with open("emotion_results.txt", "w") as file:
        file.write("Timestamp\tEmotion\tEmoji\n")
        for r in results:
            file.write(f"{r[0]}\t{r[1]}\t{r[2]}\n")


def index(request):
    return render(request, 'index.html')


def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
