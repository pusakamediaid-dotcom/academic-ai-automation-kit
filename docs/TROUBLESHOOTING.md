# 🛠️ TROUBLESHOOTING

### 1. "Model failed to load"
- **Cause**: Network issue or Hugging Face API outage.
- **Solution**: Check your internet connection or try adding a `HF_TOKEN`.

### 2. "Text too long / Memory Error"
- **Cause**: Your machine is running out of RAM during inference.
- **Solution**: Use the Google Colab version (which provides free T4 GPU/High RAM).

### 3. "Output is too generic"
- **Cause**: The input text is too vague or too short.
- **Solution**: Paste a more substantial section of the paper (e.g., the Discussion section).
