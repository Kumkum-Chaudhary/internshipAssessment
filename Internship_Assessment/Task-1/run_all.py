import subprocess

print("⏳ Running scrape_news.py...")
subprocess.run(["python", "code/scrape_news.py"], check=True)

print("⏳ Running summarize.py...")
subprocess.run(["python", "code/summarize.py"], check=True)

print("⏳ Running app.py with Streamlit...")
subprocess.run(["streamlit", "run", "app.py"], check=True)

print("✅ All steps completed successfully!")
