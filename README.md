# Shiwi

Shiwi is a Python-based personal assistant designed to help users manage tasks, set reminders, and interact with various plugins to enhance productivity.

## Table of Contents

- [Features](#features)
- [Technologies and Frameworks](#technologies-and-frameworks)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Task Management**: Create, update, and delete tasks efficiently.
- **Reminders**: Set reminders for important events and deadlines.
- **Plugin Support**: Extend functionality through a flexible plugin system.
- **Skill Integration**: Incorporate various skills to enhance assistant capabilities.

## Technologies and Frameworks

Shiwi is built using the following technologies and frameworks:

1. **Programming Language**: Python
   - Simple syntax and extensive libraries for task automation.
   
2. **Frameworks and Libraries**:
   - **Flask** (if a web interface is involved): For creating web endpoints and APIs.
   - **SpeechRecognition**: For capturing and processing audio input.
   - **pyttsx3**: For converting text to speech.
   - **Pandas/Numpy** (if any data processing is involved): For managing and analyzing data.
   
3. **Vosk**:
   - Used for offline speech recognition to provide accurate transcription.
   
4. **Natural Language Toolkit (NLTK)**:
   - Helps with parsing and understanding natural language commands (if applicable).

5. **File Storage/Database**:
   - SQLite or JSON files to manage and store tasks and reminders locally (if implemented).

6. **Unit Testing**:
   - Python’s `unittest` framework for verifying code integrity and correctness.

7. **Others**:
   - **Datetime**: To handle reminder scheduling and task deadlines.
   - **OS and Sys**: For system-level operations and integrations.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KeshavSwami21/Shiwi.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Shiwi
   ```
3. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   ```bash
   python Shiwi.py
   ```
2. **Interact with Shiwi**: Follow the on-screen prompts to manage tasks, set reminders, and utilize plugins.

## Configuration

- **Plugins**: Add your custom plugins in the `plugins` directory. Ensure they follow the required interface for seamless integration.
- **Skills**: Enhance Shiwi's capabilities by adding skill modules in the `skills` directory.
- **Model Files**: If using Vosk, ensure the required model files are downloaded and specified correctly.

## Testing

1. **Ensure All Dependencies Are Installed**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Tests**:
   ```bash
   python -m unittest discover tests
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. **Open a Pull Request**.
