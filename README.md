Gitfluent (Project Aidan) 🧠✨

Gitfluent is an AI-powered CLI tool that translates natural language into precise, executable Git commands.

Built on top of Meta's Llama-3 (8B) and fine-tuned with Unsloth, it bridges the gap between human intent and technical syntax. Whether you're a beginner afraid of git reset or a senior engineer tired of typing complex interactive rebases, Gitfluent has you covered.

🚀 Why Gitfluent?

The gap between "I want to undo my last commit" and knowing to type git reset --soft HEAD~1 is a major friction point for developers.

Gitfluent solves this by:

Understanding Intent: It knows the difference between "undo" (soft reset) and "delete" (hard reset).

Chaining Logic: It can generate multi-step commands (e.g., create a branch -> switch to it -> push upstream) in a single line.

Handling Context: It understands complex requests like resolving merge conflicts or cherry-picking specific hashes.

📥 Installation

Clone the repository:

git clone [https://github.com/YOUR_USERNAME/gitfluent.git](https://github.com/YOUR_USERNAME/gitfluent.git)
cd gitfluent


Install dependencies:
(Note: Requires a GPU-enabled environment or appropriate CPU libraries for quantization support)

pip install -r requirements.txt


🛠️ Usage

You can run Gitfluent directly from your terminal using the provided Python wrapper.

Basic Syntax:

python gitfluent.py "Your natural language request here"


Examples:

Undo a mistake:

python gitfluent.py "Undo my last commit but keep the files staged"
# Output: git reset --soft HEAD~1


Complex Branching:

python gitfluent.py "Create a new branch named feature-login and switch to it"
# Output: git checkout -b feature-login


Merge Conflicts:

python gitfluent.py "Keep the incoming changes for style.css and ignore my local version"
# Output: git checkout --theirs style.css && git add style.css


🧠 Model Details

Architecture: Llama-3 (8B Parameters)

Quantization: 4-bit (via BitsAndBytes) for efficient local inference.

Fine-Tuning Framework: Unsloth (2x faster training, 0% accuracy loss).

Dataset: Custom dataset focusing on version control edge cases, conflict resolution, and colloquial technical requests.

🔗 Download the Model Weights:
The full model weights are hosted on Hugging Face:
daimon-ml/gitfluent-llama3-8b

⚠️ Disclaimer

Gitfluent is a generative AI model. While it is fine-tuned for high accuracy, it can occasionally hallucinate or output incorrect commands.

Always review the command before executing it, especially destructive commands like reset --hard or clean -f.

Use at your own risk.

🤝 Contributing

Contributions are welcome! If you find a Git command the model struggles with, feel free to open an issue or submit a PR with new training examples.

📄 License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
