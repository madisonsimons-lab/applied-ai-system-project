# Smart Academic & Email Assistant

## Overview
This project is an AI-powered assistant that helps generate emails and academic responses using:
- Retrieval-Augmented Generation (RAG)
- Agent-based refinement workflow
- Guardrails and evaluation

## Features
- Retrieves relevant templates before generating output
- Uses an agent loop (generate → critique → refine)
- Applies safety guardrails
- Logs all outputs
- Evaluates response quality

## Setup

1. Install Python (3.8+)

2. Run the system: python main.py

## Project Structure
- retriever.py → Handles data retrieval
- agent.py → Generates and refines responses
- guardrails.py → Filters unsafe outputs
- evaluator.py → Scores outputs
- logs/ → Stores run logs

## Project Video Walkthrough
Loom Video Link: https://www.loom.com/share/088eb9d889cd4417a60e638f53b8a78f

## Example Input
Write an email to my professor about missing an assignment

## Example Output
Generated professional email with apology and refinement

## How to Run

1. Install dependencies:
pip install openai python-dotenv

2. Add your API key in a `.env` file:
OPENAI_API_KEY=your_key_here

3. Run the system:
python main.py

## Example Output

The system generates professional emails using retrieved templates, then critiques and refines them using an AI model.