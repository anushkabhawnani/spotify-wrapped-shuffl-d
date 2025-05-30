# 🎧 Shuffl'd: Your Personalized Spotify Wrapped Anytime

Shuffl'd is a web application that allows you to view your Spotify listening statistics at any time of the year. No need to wait until December to see your top artists and tracks—Shuffl'd provides a beautiful and interactive interface to explore your music habits whenever you like.

## 🚀 Features
* **Real-Time Spotify Stats:** Access your top artists and tracks based on your listening history.
* **Interactive UI:** Enjoy a user-friendly interface designed with HTML, CSS, and Bootstrap.
* **Spotify Integration:** Authenticate securely with your Spotify account to fetch personalized data.
* **Year-Round Access:** Unlike the annual Spotify Wrapped, Shuffl'd lets you check your stats anytime.

## 🛠️ Technologies Used
* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Python
* **API:** Spotify Web API

## 📁 Project Structure
```
shuffld/
│
├── static/                     # Static files like CSS
│   └── css/
│       └── styles.css
│
├── templates/                  # HTML templates
│   ├── index.html
│   ├── artists_page.html
│   └── tracks_page.html
│
├── .env                        # Environment variables (client ID, secret)
├── main.py                     # Main application logic (Flask)
└── requirements.txt            # Python dependencies
```

## 🧪 Getting Started
### Prerequisites
* Python 3.x installed on your machine
* A Spotify Developer Account to obtain your CLIENT_ID and CLIENT_SECRET

### Installation
1. Clone the repository:
```
git clone https://github.com/anushkabhawnani/spotify-wrapped-shuffl-d.git
cd spotify-wrapped-shuffl-d
```

2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Set up environment variables:
Create a .env file in the root directory and add your Spotify API credentials:
```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://localhost:8888/callback
```

5. Run the application:
```
python main.py
```
Open your browser and navigate to http://localhost:8888 to use the application.

## 📸 Screenshots

[Check out the website here and check out your Spotify Stats!](https://shuffld.onrender.com/)

(This link does take a long time to load as it has been deployed for free but it does work just fine! It has not been made mobile responsive yet.)

### Main Page
![Main Page](https://github.com/user-attachments/assets/783715db-c0d7-46b1-8821-572d6a40f2a5)

### Spotify Authorization
![Spotify Authorization](https://github.com/user-attachments/assets/ab16d3cd-d5c6-47e0-a9f3-1b12ad9c54ad)

### Top Artists Page
![Top Artists Page](https://github.com/user-attachments/assets/20ec8ea4-397c-4f81-a910-3b240d6c43da)

### Top Tracks Page
![Top Tracks Page  ](https://github.com/user-attachments/assets/50a951bc-d3ad-4bb2-8fa1-c233c60b4335)

## 🚀 Future Work
* **Mobile Responsiveness:** Optimize the user interface for mobile and tablet devices using advanced frontend techniques (media queries, responsive layouts, etc.).
* **User Personalization:** Allow users to save their sessions, compare listening habits over time, or generate shareable summaries.
* **Analytics Dashboard:** Provide detailed insights with charts/graphs of listening trends, genres, and artist discovery over time.

## 🙏 Acknowledgements
* **Spotify Web API** – for enabling access to real-time music data.
* **Flask** – lightweight Python web framework used for routing and backend logic.
* **Bootstrap** – for responsive and modern UI components.

## 📬 Contact
If you have questions, feedback, or would like to collaborate, feel free to reach out!
* [Email](anushkab1411@gmail.com)
* [Linkedin](https://www.linkedin.com/in/anushka-bhawnani-0a3207316/)
* [GitHub](https://github.com/anushkabhawnani)
