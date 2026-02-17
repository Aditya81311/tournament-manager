# 🎮 eSports Arena - Tournament Management Platform

A modern, feature-rich tournament management web application built with Flask. Manage games, teams, tournaments, and players with a stunning cyberpunk-inspired UI.

## ✨ Features

### Implemented Features
- **User Authentication**
  - User registration and login
  - Role-based access (Player/Admin)
  - Session management
  
- **Games Management**
  - View all games
  - Add/Edit/Delete games (Admin only)
  - Multiple game genres support

- **Teams Management**
  - Create teams with automatic captain assignment
  - Join existing teams
  - View team details and members
  - Leave teams (non-captains)
  - Team member tracking

- **Tournaments Management**
  - Create tournaments (Admin only)
  - View tournament details
  - Match scheduling
  - Tournament status tracking (Upcoming/Active/Completed)

- **Dashboard**
  - Personalized player dashboard
  - Quick access to user's teams
  - Profile management

### Under Development (Placeholders Ready)
- Leaderboard functionality
- Match results and scoring
- Team statistics
- Player achievements

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
tournament_app/
├── app.py                 # Main Flask application with routes
├── models.py              # Database models and operations
├── requirements.txt       # Python dependencies
├── database.db           # SQLite database (auto-created)
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── register.html     # Registration form
│   ├── login.html        # Login form
│   ├── dashboard.html    # User dashboard
│   ├── profile.html      # User profile
│   ├── games.html        # Games listing
│   ├── add_game.html     # Add game form
│   ├── edit_game.html    # Edit game form
│   ├── teams.html        # Teams listing
│   ├── create_team.html  # Create team form
│   ├── team_details.html # Team details page
│   ├── tournaments.html  # Tournaments listing
│   ├── create_tournament.html # Create tournament form
│   ├── tournament_details.html # Tournament details page
│   └── leaderboard.html  # Leaderboard (placeholder)
└── static/
    ├── css/             # CSS files (inline in templates)
    └── js/              # JavaScript files (inline in templates)
```

## 🗄️ Database Schema

The application uses SQLite with the following tables:

- **users**: User accounts and authentication
- **games**: Available games
- **teams**: Team information
- **team_members**: Team membership tracking
- **tournaments**: Tournament details
- **matches**: Match scheduling
- **leader_board**: Leaderboard data (future implementation)

## 🎨 Design Features

- **Cyberpunk/Gaming Aesthetic**: Neon colors, glowing effects, modern gradients
- **Responsive Design**: Works on desktop and mobile devices
- **Animated UI**: Smooth transitions and hover effects
- **Dark Theme**: Optimized for extended use

## 👥 User Roles

### Player (Default)
- Register and login
- Create and join teams
- View games and tournaments
- Access personal dashboard

### Admin
- All player permissions
- Add/Edit/Delete games
- Create tournaments
- Manage platform content

## 🔐 Default Admin Setup

To create an admin user, register normally and then update the database:

```python
import sqlite3
conn = sqlite3.connect('database.db')
conn.execute("UPDATE users SET user_role = 'admin' WHERE user_email = 'your@email.com'")
conn.commit()
conn.close()
```

## 📝 Usage Guide

### For Players:
1. Register an account
2. Login to access your dashboard
3. Browse or create teams
4. Join teams to participate
5. View upcoming tournaments

### For Admins:
1. Login with admin credentials
2. Add games to the platform
3. Create tournaments
4. Manage platform content

## 🔧 Configuration

### Secret Key
Change the secret key in `app.py` for production:
```python
app.secret_key = 'your-secure-secret-key-here'
```

### Database
The application uses SQLite by default. To use a different database:
1. Modify the `get_db_connection()` function in `models.py`
2. Update the connection string

## 🚧 Future Enhancements

- Complete leaderboard implementation
- Match result recording
- Real-time match updates
- Team statistics and analytics
- Player achievements system
- Tournament brackets visualization
- Email notifications
- Advanced search and filters
- Team chat/messaging
- Profile customization

## 🐛 Known Issues

- Password storage is currently plain text (should implement hashing)
- No email verification
- Limited error handling in some edge cases

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📞 Support

For issues or questions, please create an issue in the repository.

---

**Built with ⚡ by the eSports Arena Team**
