# 🏨 Hotel Booking App Using OOP

This is a Python-based console application that simulates a hotel booking system using Object-Oriented Programming principles. It allows users to browse available hotels, make bookings, and simulate payments using stored card data. All user actions are processed through a structured, class-based backend for better maintainability and modularity.

---

## 📑 Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Page Structure](#page-structure)
  - [Color Scheme & Typography](#color-scheme--typography)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Planned Improvements](#planned-improvements)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Libraries Used](#libraries-used)
- [Project Files](#project-files)
- [Installation & Usage](#installation--usage)
  - [How to Run](#how-to-run)
  - [Modifying the Input File](#modifying-the-input-file)
- [Testing](#testing)
- [Credits](#credits)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

---

## 🧑‍💼 User Experience (UX)

### 🧾 User Stories

**As a first-time user**, I want to:

- Understand what hotels are available.
- See basic information like hotel name, location, and availability.
- Book a room using a simple input process.

**As a returning user**, I want to:

- Quickly find the hotel I previously used.
- Use stored card details to book again.

**As an administrator or developer**, I want to:

- Easily update the hotel, card, or security information via CSV files.
- Extend the app by adding more hotel functionality.

---

## 🎨 Design

### 🗂 Page Structure

Since this is a CLI (Command Line Interface) project, there are no pages, but interaction occurs step-by-step in the terminal with clear, user-friendly prompts.

1. Welcome message and hotel list
2. Prompt for hotel selection
3. Input for user name and booking confirmation
4. Payment processing
5. Booking confirmation and ticket

### 🌈 Color Scheme & Typography

- **Color Scheme**: Terminal-based. Colorized output could be added in future enhancements using libraries like `colorama`.
- **Typography**: Uses default system terminal fonts.

---

## 🚀 Features

### ✅ Implemented Features

- **OOP Architecture**: Code organized into classes for `Hotel`, `CreditCard`, and `ReservationTicket`.
- **Hotel Listing**: Dynamically loads and displays hotel data from a CSV file.
- **Room Availability**: Updates availability upon booking.
- **User Reservation**: Collects user name and preferred hotel.
- **Payment Simulation**: Verifies card and security code via CSV files.
- **Ticket Generation**: Generates a text-based confirmation receipt after booking.

### 🛠️ Planned Improvements

- GUI implementation using Tkinter or PyQt.
- Input validation and error handling.
- Enhanced booking management (e.g., multiple nights, number of guests).
- User authentication and profile creation.
- Logging and audit trail for all transactions.
- Migration from CSV to SQLite or PostgreSQL.

---

## 💻 Technologies Used

### 🧑‍💻 Languages Used

- Python 3.x

### 📚 Libraries Used

- `csv` – for reading/writing structured data.
- `os` – for clearing screen and file management.
- `datetime` – for timestamps and ticket issuance.

_No external packages are required._

---

## 🗃 Project Files

```bash
hotel-booking-app-using-oop/
│
├── main.py # Main application logic and CLI interface
├── hotels.csv # Hotel records (ID, name, location, availability)
├── cards.csv # Valid credit card numbers for simulated payments
├── card_security.csv # Security codes associated with each card
├── requirements.txt # Placeholder for future dependencies
└── README.md # Project documentation
```

---

## 🛠 Installation & Usage

### ⚙️ How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/mahmudurmahid/hotel-booking-app-using-oop.git
cd hotel-booking-app-using-oop
```

2. Run the app:

```bash
python main.py
```

3. Follow the prompts:

- Choose a hotel
- Enter your name
- Input your credit card number and security code
- Receive a booking confirmation

### 🧾 Modifying the Input File

To add or change hotels:

- Open hotels.csv
- Add a new line following the format:

```bash
hotel_id,hotel_name,location,availability
```

To update card details:

- Edit cards.csv and card_security.csv respectively.

## ✅ Testing

### Manual Testing Summary

- ✅ Hotel list loads correctly.
- ✅ Booking a room updates availability.
- ✅ Invalid hotel input triggers an error message.
- ✅ Card validation fails on incorrect input.
- ✅ Successful card entry triggers ticket confirmation.

### Suggested Future Tests

- Unit tests for class methods (e.g., Hotel.book())
- Integration test for booking + card process
- Edge case tests (e.g., booking when no availability)

## 🙌 Credits

### 👨‍💻 Author

This project was created and maintained by **Mahmudur mahid**. It serves as a portfolio-level demonstration of object-oriented programming principles applied in a practical Python application. Mahmudur is passionate about developing intuitive, educational, and well-structured backend systems and enjoys exploring how fundamental concepts like OOP can be used in real-world problem solving.

- [GitHub Profile](https://github.com/mahmudurmahid)
- [LinkedIn](#https://www.linkedin.com/in/mahmudur-mahid-a4aa78162/)

### 🙏 Acknowledgements

This project draws conceptual and technical influence from a variety of sources and individuals:

#### 🧠 Educational Inspiration

- **Python OOP Courses**

  - [Corey Schafer](https://www.youtube.com/user/schafer5) – for deep dives into Python’s class-based structure and clean coding practices.
  - [freeCodeCamp Python Tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw) – provided foundational insights into Python application building.
  - [Programming with Mosh](https://www.youtube.com/c/programmingwithmosh) – useful for understanding application flow and simulation logic.

- **CS Fundamentals**
  - Concepts of encapsulation, abstraction, and modularity are aligned with classic OOP principles found in most university-level CS101 courses.

#### 🧰 Tooling & Libraries

- The `csv` and `datetime` modules used in this app are part of Python’s robust standard library, requiring no external installation.

#### 💬 Community Support

- [Stack Overflow](https://stackoverflow.com/) – invaluable for answering specific Python/OOP questions during development.
- [r/learnpython](https://www.reddit.com/r/learnpython/) on Reddit – helpful feedback and advice from Python learners and mentors.
- GitHub discussions and repositories from developers building CLI apps with class-based structure.

#### 📝 Content & Structural References

- README file formatting was inspired by high-quality open-source projects such as:
  - [Django](https://github.com/django/django)
  - [Real Python Projects](https://realpython.com/)
  - Markdown best practices from [GitHub Docs](https://docs.github.com/en)

### 💬 Feedback & Contributions

Feedback, bug reports, and pull requests are **very welcome**! If you have suggestions for how this project could be improved — whether that’s additional features, better abstraction, or even UI upgrades — don’t hesitate to fork and contribute.
