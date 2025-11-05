# Sky Library Membership System

This project is a simple terminal-based library membership and entry validation system. Users can register for different subscription plans (daily, weekly, monthly, yearly, VIP) and then use their generated user code to enter the library. The program also records visit times.

---

## Features

* New user registration with 5 types of subscription plans.
* Subscription validity based on the length of the generated user code.
* Visiting time tracking for each entry.
* Payment simulation using a linked local bank storage file.
* Data stored in `Library_store.json`.

---

## Subscription Plans & Costs

| Subscription | Cost (₹) | Validity |
| ------------ | -------- | -------- |
| Daily        | 50       | 1 day    |
| Weekly       | 150      | 7 days   |
| Monthly      | 500      | 30 days  |
| Yearly       | 5000     | 365 days |
| VIP          | 7000     | Lifetime |

Each plan generates a **User Code** of a specific digit-length, which is used later to verify subscription validity.

---

## How It Works

### Running the Program

Run:

```
python main.py
```

You will be asked whether you are a new user or an existing user.

### New User Registration

If selecting `Yes`:

1. Enter name
2. Enter mobile number
3. Choose subscription
4. Make payment
5. Receive your unique **User Code**

### Existing User Login

Enter:

* Name
* Mobile number
* User Code

The system will:

* Check subscription validity
* Allow entry and record visit time

---

## Payment System

This system uses a JSON-based bank storage file.

Default path inside code:

```
D:\Code\Python\Suraj of python\Old_Bank\CBSE_Store.json
```

Ensure this file exists and contains accounts in the following format:

```
[
  {
    "Account Number": "123456789012",
    "PIN": 1234,
    "Bank Balance": 5000
  }
]
```

### Sample Test Bank Account

You may create a sample account for testing:

```
Account Number: 123456789012
PIN: 237899
Balance: Any positive amount
```

Or check another repository named **Bank** to generate your own.

---

## Data Storage

This program stores user membership and visit history in:

```
Library_store.json
```

Structure example:

```
[
  {
    "Name": "John Doe",
    "Mobile Number": 9876543210,
    "User_code": 12345678,
    "Time": 1730000000.00,
    "Visiting": [
       {"From": "05-11-2025, 10:00:00", "To": "05-11-2025, 12:30:00"}
    ]
  }
]
```

---

## Notes & Tips

* Do **not** share your user code.
* Ensure your bank file path is correct.
* Do not remove or manually modify `Library_store.json` unless needed.

---

## Future Enhancements (Optional Ideas)

* Add book borrowing system
* Add fine calculation for overdue users
* Add GUI using Tkinter or PyQt

---

## License

This project is free to modify and use for learning and educational purposes.

---

If you'd like, I can now:

* Create a `.gitignore` file
* Create a sample `Library_store.json`
* Convert this system to use hashed PINs instead of plain numbers.
