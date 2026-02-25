# 🏆 Tournament Manager

A full-stack web application built with **Flask & SQLite** for managing competitive tournaments. Supports team creation, tournament scheduling, match tracking, score entry, and a live leaderboard — all behind a role-based authentication system.

---

## 📸 Features

- 🔐 **Role-based Auth** — Admin and Player roles with session management
- 🎮 **Game Management** — Add, update, and delete games
- 👥 **Team Management** — Create teams, assign captains, join existing teams
- 🏆 **Tournament Management** — Create and manage tournaments with start/end dates and status
- 📅 **Match Scheduling** — Schedule matches between teams with round tracking
- 📊 **Score Entry** — Admin can enter and update match scores
- 📈 **Leaderboard** — Dynamic rankings by points, wins, and score difference
- 📱 **Responsive UI** — Works on desktop and mobile

---

## 🛠 Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Backend    | Python, Flask               |
| Database   | SQLite                      |
| Frontend   | Bootstrap 5, Bootstrap Icons |
| Templating | Jinja2                      |
| Styling    | Custom CSS (Gradients + Animations) |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/tournament-manager.git
cd tournament-manager
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📁 Project Structure

```
tournament-manager/
│
├── app.py                  # Main Flask application & routes
├── database.db             # SQLite database (auto-created)
├── requirements.txt
│
├── static/
│   └── style.css           # Custom CSS with gradients & animations
│
└── templates/
    ├── base.html            # Base layout with navbar & footer
    ├── home.html            # Landing page
    ├── index.html           # Dashboard (login required)
    ├── login.html
    ├── register.html
    ├── create_admin.html
    ├── games.html
    ├── add_games.html
    ├── update_games.html
    ├── delete_games.html
    ├── list_teams.html
    ├── create_teams.html
    ├── update_teams.html
    ├── delete_teams.html
    ├── join_teams.html
    ├── user_teams.html
    ├── list_tournaments.html
    ├── create_tournament.html
    ├── update_tournaments.html
    ├── delete_tournament.html
    ├── list_matches.html
    ├── create_match.html
    ├── update_match.html
    ├── delete_match.html
    ├── add_scores.html
    └── leader_board.html
```

---

## 👤 User Roles

| Role   | Permissions                                                  |
|--------|--------------------------------------------------------------|
| Admin  | Full access — manage games, teams, tournaments, matches, scores |
| Player | Join/create teams, view tournaments, matches, leaderboard    |

---

## 📊 Points System

| Result | Points |
|--------|--------|
| Win    | 3      |
| Loss   | 0      |

Teams are ranked by **points**, then by **score difference** (Score For − Score Against).

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ using Flask & SQLite