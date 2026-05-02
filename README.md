# 📂 Secure PDF Merger

## What is this?

Basically, when I was applying for the NHL Stenden program, I ran into a super frustrating hurdle: online application portals are great, but they often force you to upload different documents—like my diploma, transcripts, and ID—into completely separate sections. The worst part? They only let you upload **one file per section**.

To get everything processed in one go, I realized I needed a reliable way to merge all those individual PDFs into one clean, cohesive document.

Since I'm really interested in cybersecurity and privacy (and honestly, dealing with my personal academic data online feels sketchy), I decided to build this tool myself—to ensure I had total control over my documents and they never had to leave my machine. 🛡️

---

## 🔒 Why Is This Better? (The Philosophy)

Most web-based "PDF Merger" tools are super convenient, but that convenience comes at a massive privacy cost. You have to upload your sensitive personal data (transcripts, grades, etc.) to some third-party server you don't trust. **That is a no-go.**

This tool operates on a strict **Privacy by Design** model:

*   **💻 100% Local Execution:** Your data never touches the internet or any outside server. All processing happens right here, on your laptop.
*   **🚫 Zero Third-Party Risk:** No web uploads means no risk of data breaches, document retention, or sketchy external logging.
*   **🔎 Transparent Codebase:** The logic is open-source because I want it to be auditable! You should know exactly how your files are being handled.

This isn't just about merging PDFs; it's a demonstration of prioritizing personal data security while solving a real, messy-world problem.

---

## 🛠 Getting Set Up (Requirements)

To run these scripts, you'll need Python installed on your system. Then, open your terminal or command prompt and install the required libraries:

```bash
pip install pypdf tkinterdnd2



🚀 How to Use It
I included two versions because different situations require different workflows—a super easy graphical interface or a quick batch script.

🖼️ 1. The GUI Version (merger_app.py) — Recommended!
This version is way more user-friendly and uses the native drag-and-drop function, which is much smoother than using the terminal.

Run it: python merger_app.py
A little window titled "Quick PDF Merger" will pop up.
Just drag all your PDFs (transcripts, IDs, diplomas, etc.) directly onto the gray drop zone.
The system will automatically open a file explorer asking you where you want to save the final merged document and what you want to name it.
When it’s done, you get a confirmation message! 🎉
💻 2. The Mini Script Version (merger_mini.py) — For Quick Batches
If you prefer staying in the terminal or need to merge files in a quick batch run, use this script.

Make sure all the PDFs you want to combine are sitting in the same directory as merger_mini.py.

Open merger_mini.py and edit the last line to list your filenames:

# Example: Merging a diploma, transcript, and ID
merge_pdfs("final_document.pdf", "my_diploma.pdf", "transcript_fall23.pdf").
Run the script from the terminal: python merger_mini.py

Success! Your new PDF will be waiting in that folder.
