from flask import Flask, render_template

app = Flask(__name__)

# These are the ten projects selected from the public repository names visible
# on your GitHub profile/screenshots. Review descriptions and technology labels
# against each repository README before final submission.
projects = [
    {
        "title": "Speech Recognition",
        "description": "A Python project focused on recognizing speech and working with audio input.",
        "tech_stack": ["Python", "Speech Recognition", "Audio"],
        "github_url": "https://github.com/garamhasan75-ship-it/Speech-Recognition",
        "image": "images/speech-recognition.png",
    },
    {
        "title": "Object Detection Based on Colour",
        "description": "A computer-vision project that identifies objects or regions based on colour.",
        "tech_stack": ["Python", "OpenCV", "Computer Vision"],
        "github_url": "https://github.com/garamhasan75-ship-it/Object-detection-based-on-colour",
        "image": "images/object-detection.png",
    },
    {
        "title": "Gesture Volume Control",
        "description": "A hand-gesture project using MediaPipe and OpenCV to control system volume.",
        "tech_stack": ["Python", "MediaPipe", "OpenCV"],
        "github_url": "https://github.com/garamhasan75-ship-it/Gesture-Volume-Control-using-MediaPipe-and-OpenCV",
        "image": "images/gesture-volume-control.png",
    },
    {
        "title": "Face Detection using OpenCV",
        "description": "A Python computer-vision project for detecting faces in images or camera input.",
        "tech_stack": ["Python", "OpenCV", "Computer Vision"],
        "github_url": "https://github.com/garamhasan75-ship-it/Face-Detection-using-OpenCV-in-Python",
        "image": "images/face-detection.png",
    },
    {
        "title": "News Article Summarizer",
        "description": "A project intended to summarize news articles into shorter text.",
        "tech_stack": ["Python", "Text Processing"],
        "github_url": "https://github.com/garamhasan75-ship-it/News-Article-Summarizer",
        "image": "images/news-summarizer.png",
    },
    {
        "title": "Sales Data Analysis",
        "description": "A Python project for exploring sales data and presenting useful summaries.",
        "tech_stack": ["Python", "Data Analysis"],
        "github_url": "https://github.com/garamhasan75-ship-it/sales-data-analysis",
        "image": "images/sales-analysis.png",
    },
    {
        "title": "Professional Language Translator GUI",
        "description": "A desktop translation application built with a Tkinter graphical interface.",
        "tech_stack": ["Python", "Tkinter", "GUI"],
        "github_url": "https://github.com/garamhasan75-ship-it/-Professional-Language-Translator-Tkinter-GUI",
        "image": "images/language-translator.png",
    },
    {
        "title": "Python Weather Info App",
        "description": "A Python application that presents weather information.",
        "tech_stack": ["Python", "Weather Information"],
        "github_url": "https://github.com/garamhasan75-ship-it/Python-Weather-Info-App",
        "image": "images/weather-app.png",
    },
    {
        "title": "Directory File Organizer",
        "description": "A Python utility that helps organize files into directory categories.",
        "tech_stack": ["Python", "Automation", "File Handling"],
        "github_url": "https://github.com/garamhasan75-ship-it/dirx-file-organizer",
        "image": "images/file-organizer.png",
    },
    {
        "title": "Word Frequency",
        "description": "A text-processing project that counts how often words occur in text.",
        "tech_stack": ["Python", "Collections", "Text Processing"],
        "github_url": "https://github.com/garamhasan75-ship-it/word_frequency",
        "image": "images/word-frequency.png",
    },
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
