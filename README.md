🚀 Generative AI Projects – Local LLM + Fine-Tuning

This repository contains hands-on projects focused on understanding how Large Language Models (LLMs) work in real-world environments — both for local inference and fine-tuning.
These projects were built as part of practical learning in Generative AI systems, covering model deployment, API interaction, GPU training, and parameter-efficient fine-tuning.

📌 Project 1: Local LLM Chatbot (Ollama + Streamlit)

🔎 Overview

<img width="800" height="648" alt="llm" src="https://github.com/user-attachments/assets/64064a41-810b-46fc-b59e-51c709a89c0f" />

This project demonstrates how to run a lightweight LLM locally and build a simple interactive chatbot interface around it.
Instead of relying on cloud APIs, the model runs directly on a local machine.

🛠 Technologies Used

Ollama
Streamlit
TinyLlama (1B parameters)
Python

⚙️ How It Works

Ollama runs TinyLlama locally.
A Streamlit app provides a chat interface.
User prompts are sent to Ollama’s local API.
The model generates and returns responses in real time.

▶️ How to Run

Install dependencies:
pip install streamlit requests

Pull the model:
ollama pull tinyllama

Run the app:
streamlit run app.py

Then open the local URL shown in your terminal.

💡 What This Project Demonstrates
Running LLMs locally
API-based model interaction
Prompt handling and response generation
Lightweight AI UI development
Understanding inference workflows

📌 Project 2: Fine-Tuning an LLM with Unsloth

🔎 Overview
<img width="800" height="554" alt="t2" src="https://github.com/user-attachments/assets/112b5a52-ebb7-4e3f-b4ef-eed2af7086de" />


This project demonstrates how to fine-tune a quantized LLM using LoRA (Low-Rank Adaptation) for instruction-based tasks.
The training was performed using GPU acceleration.

🛠 Technologies Used

Unsloth
Google Colab
PyTorch
Transformers
LoRA
Tesla T4 GPU

⚙️ What Was Done

Loaded a 4-bit quantized base model
Prepared an instruction-style dataset
Applied LoRA configuration
Performed parameter-efficient fine-tuning
Generated outputs for evaluation

💡 Concepts Practiced

PEFT (Parameter-Efficient Fine-Tuning)
LoRA adaptation
GPU memory optimization
Instruction formatting
Model evaluation after training

🧠 Key Learnings

Through these projects, I gained practical experience in:
The difference between inference and training
Running LLMs locally vs cloud usage
Efficient fine-tuning with limited GPU memory
Model architecture basics
Prompt engineering
Debugging real-world AI workflows

📂 Repository Structure
.
├── app.py
├── fine_tuning_notebook.ipynb
└── README.md
🎯 Why This Matters
Understanding LLMs is not just about using APIs.

This repository demonstrates:
Local model deployment
Direct API communication
GPU-based fine-tuning
Practical implementation of LoRA
End-to-end LLM workflow knowledge

🔮 Future Improvements
Deploy chatbot to a cloud environment
Train on a larger custom dataset
Implement Retrieval-Augmented Generation (RAG)
Optimize inference speed
Experiment with larger models

 Author
Ayesha Abbasi
Generative AI Enthusiast | Learning by Building
