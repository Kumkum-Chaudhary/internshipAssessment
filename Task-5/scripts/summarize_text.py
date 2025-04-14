def summarize_text(input_path, output_path, max_sentences=10):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = text.split(". ")
    summary = ". ".join(sentences[:max_sentences])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary.strip())

    print("✅ Summary saved to", output_path)

if __name__ == "__main__":
    summarize_text("data/extracted_text.txt", "data/summary.txt")
