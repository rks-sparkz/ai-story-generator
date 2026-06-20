# AI Story Generator

A modular, production-grade Python application that leverages OpenAI's structured outputs to generate creative stories based on user-defined characters and genres.

## 🚀 Project Overview
This project utilizes a decoupled, object-oriented architecture split cleanly across data validation models (`Pydantic`), configuration managers (`python-dotenv`), pipeline orchestrators, and third-party API service engines. It ensures responses strictly match a targeted JSON matrix layout.

## 🛠️ Environment Setup & Installation
1. Clone the repository and navigate into the directory.
2. Initialize and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate