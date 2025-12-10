# 🎯 Quiz Game Using Basic OOP

An interactive command-line quiz game built with Python that demonstrates fundamental Object-Oriented Programming (OOP) concepts. This project features a True/False trivia quiz with automated scoring and user-friendly feedback.

## 📋 Overview

This quiz game is a beginner-friendly Python project that showcases core OOP principles including classes, objects, methods, and attributes. The game presents users with a series of True/False questions, validates their answers, tracks their score, and provides immediate feedback after each question.

## ✨ Features

- **Interactive Gameplay**: Command-line interface for answering True/False questions
- **Automated Scoring**: Real-time score tracking throughout the quiz
- **Instant Feedback**: Immediate validation of answers with correct answer display
- **Modular Design**: Clean separation of concerns with dedicated classes for different functionalities
- **Extensible Question Bank**: Easy to add or modify questions
- **Progress Tracking**: Shows current question number and running score

## 🏗️ Project Structure

The project follows OOP best practices with a modular architecture:

```
quiz-game-using-basic-OOPs/
├── main.py              # Entry point and game initialization
├── question_model.py    # Question class definition
├── quiz_brain.py        # QuizBrain class for game logic
├── data.py              # Question data storage
└── README.md            # Project documentation
```

### File Descriptions

#### `main.py`
The main entry point that:
- Imports required modules
- Creates Question objects from question data
- Initializes the QuizBrain
- Runs the game loop
- Displays final score

#### `question_model.py`
Defines the `Question` class with:
- `text`: The question text
- `answer`: The correct answer (True/False)

#### `quiz_brain.py`
Contains the `QuizBrain` class that handles:
- Question navigation
- Answer checking
- Score tracking
- User interaction

#### `data.py`
Stores the question bank as a list of dictionaries with:
- Question text
- Correct answers

## 🎮 How It Works

### Class Structure

#### 1. Question Class
```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
```

Simple data model that encapsulates question information.

#### 2. QuizBrain Class
```python
class QuizBrain:
    def __init__(self, quiz_list):
        self.question_number = 0
        self.score = 0
        self.quiz_list = quiz_list
    
    def next_question(self):
        # Displays question and gets user input
    
    def still_has_questions(self):
        # Checks if more questions remain
    
    def check_answer(self, user_answer, correct_answer):
        # Validates answer and updates score
```

Manages the quiz flow, scoring, and user interaction.

### Game Flow

1. **Initialization**: Questions are loaded from `data.py` and converted to Question objects
2. **Quiz Loop**: 
   - Display current question
   - Get user input (True/False)
   - Validate answer
   - Update score
   - Show feedback
   - Move to next question
3. **Completion**: Display final score when all questions are answered

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic understanding of Python syntax
- Command-line/terminal access

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/lakumsaicharan/quiz-game-using-basic-OOPs.git
cd quiz-game-using-basic-OOPs
```

2. **Run the game**
```bash
python main.py
```

### Usage

1. Run the game using `python main.py`
2. Read each question carefully
3. Type `True` or `False` as your answer
4. Press Enter to submit
5. View immediate feedback and your current score
6. Complete all questions to see your final score

## 📝 Sample Output

```
Q.1: A slug's blood is green. (True/False): True
You are right! Your score is: 1/1
The correct answer was: True

Q.2: The loudest animal is the African Elephant. (True/False): False
You are right! Your score is: 2/2
The correct answer was: False

...

You've completed the quiz!
Your final score was: 10/13
```

## 🎓 OOP Concepts Demonstrated

### 1. **Classes and Objects**
- `Question` class models individual quiz questions
- `QuizBrain` class encapsulates quiz logic
- Multiple Question objects created from data

### 2. **Encapsulation**
- Data (question text, answer) and methods bundled in classes
- Internal state managed through methods

### 3. **Attributes and Methods**
- Instance attributes: `question_number`, `score`, `quiz_list`
- Instance methods: `next_question()`, `still_has_questions()`, `check_answer()`

### 4. **Constructor (`__init__`)**
- Initialize object state when creating instances
- Set up initial values for attributes

### 5. **Method Calls**
- Objects interact through method invocations
- Clean API for quiz operations

## 🔧 Customization

### Adding More Questions

Edit `data.py` to add new questions:

```python
question_data = [
    {"text": "Your question here", "answer": "True"},
    # Add more questions...
]
```

### Modifying Question Format

1. Update the `Question` class in `question_model.py`
2. Modify the `check_answer()` method in `quiz_brain.py`
3. Update `data.py` structure accordingly

### Changing Difficulty

Replace questions in `data.py` with:
- Easier questions for beginners
- Harder questions for advanced players
- Topic-specific questions (science, history, etc.)

## 💡 Learning Outcomes

After working with this project, you'll understand:

- How to design and implement Python classes
- Proper use of `__init__` constructors
- Creating and using object instances
- Method definition and invocation
- Managing object state with attributes
- Separating data, models, and logic
- Building interactive command-line applications
- Implementing game loops

## 🔮 Future Enhancements

- [ ] Add multiple choice questions
- [ ] Implement difficulty levels (Easy/Medium/Hard)
- [ ] Add timer for each question
- [ ] Include question categories
- [ ] Store high scores to a file
- [ ] Add a leaderboard system
- [ ] Create a GUI version using Tkinter
- [ ] Fetch questions from an API (e.g., Open Trivia DB)
- [ ] Add hints system
- [ ] Implement lives/chances mechanism
- [ ] Add sound effects
- [ ] Support for multiple players

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new questions
- Report bugs
- Suggest features
- Improve code quality
- Enhance documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Sai Charan Lakum**
- GitHub: [@lakumsaicharan](https://github.com/lakumsaicharan)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/lakumsaicharan)

## 🙏 Acknowledgments

- Inspired by Python OOP tutorials and best practices
- Quiz questions sourced from general trivia knowledge
- Built as part of learning Python and Object-Oriented Programming

---

⭐ Star this repository if you found it helpful for learning OOP in Python!
