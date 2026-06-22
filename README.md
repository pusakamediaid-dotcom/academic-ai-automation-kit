# Academic AI Automation Kit 🎓

Welcome to the engine of the **Academic AI OS**. This repository provides the technical tools to automate the boring parts of research, allowing you to focus on synthesis and critical analysis.

## 🚀 Features
- **AI Paper Summarizer**: Leverages State-of-the-Art (SOTA) models from Hugging Face to condense complex academic papers.
- **Key Insight Extractor**: Quickly identifies the core arguments of a text.
- **Cloud Ready**: Designed to run on local machines or Google Colab.

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/academic-ai-automation-kit.git
cd academic-ai-automation-kit
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Your Hugging Face Token
The toolkit requires a Hugging Face API token to access the models.
- Get your token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
- Set it as an environment variable:
  ```bash
  export HF_TOKEN='your_token_here'
  ```

### 4. Run the Toolkit
```bash
python main.py
```

## 📚 How it fits into the Academic AI OS
This toolkit is the "Execution Layer." 
1. Find a paper $\rightarrow$ **Notion**
2. Process with this **GitHub Toolkit** $\rightarrow$ **Hugging Face Models**
3. Store results back in **Notion**

## License
MIT License
