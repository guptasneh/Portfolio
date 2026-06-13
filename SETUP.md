# Portfolio Database Integration Setup

## Prerequisites
- Python 3.8+
- MongoDB running locally or accessible
- pip package manager

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Check Database Connection
```bash
python test_db.py
```

### 3. Start the Flask Server
```bash
python app.py
```

Expected output:
```
============================================================
🚀 Portfolio Backend Server
============================================================
📡 Server running at: http://localhost:5000
🗄️  Database: MongoDB at mongodb://localhost:27017/
============================================================
```

### 4. Access Your Portfolio
- Open browser and go to: `http://localhost:5000`
- Your portfolio will load with database integration

## API Endpoints

### Health Check
```
GET /api/health
```
Response: `{"status": "ok", "message": "Server is running"}`

### Submit Contact Form
```
POST /api/contact
```
Body:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Project Inquiry",
  "message": "Your message here"
}
```
Response: `{"success": true, "message": "Contact message received successfully!"}`

### Submit Feedback
```
POST /api/feedback
```
Body:
```json
{
  "rating": 5,
  "comments": "Great portfolio!"
}
```
Response: `{"success": true, "message": "Feedback submitted successfully!"}`

## Database Collections

### contacts
Stores contact form submissions:
```
{
  "_id": ObjectId,
  "name": string,
  "email": string,
  "subject": string,
  "message": string,
  "created_at": datetime
}
```

### feedback
Stores user feedback:
```
{
  "_id": ObjectId,
  "rating": number (1-5),
  "comments": string,
  "created_at": datetime
}
```

## Troubleshooting

### MongoDB Connection Failed
- Ensure MongoDB is running: `mongod`
- Check MONGO_URI in `.env` file
- Run `python test_db.py` to verify connection

### Port 5000 Already in Use
Change port in `app.py`:
```python
app.run(debug=True, host='localhost', port=8000)
```

### CORS Errors
- Ensure `Flask-CORS` is installed
- Check CORS is enabled in `app.py`

## Files Structure
```
portfolio/
├── app.py              # Flask backend server
├── db.py               # MongoDB database functions
├── db.py               # Database connection setup
├── index.html          # Frontend
├── js/
│   ├── contact.js      # ✅ Updated - sends to backend API
│   └── ... (other JS files)
├── css/                # Stylesheets
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
└── test_db.py         # Database test script
```

## Next Steps
1. ✅ Database is ready
2. ✅ Backend server is ready
3. ✅ Contact form integrated
4. 📋 Add feedback form integration (optional)
5. 🎨 Customize API responses as needed
