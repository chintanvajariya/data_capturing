# Double Screen Data Capture

## Purpose

In today's research environment, data-collecting hardware often comes with proprietary software that's not only costly but also demands valuable time for manual data recording. For instance, analyzing the 2e- ARPES' pressure values requires meticulous attention, diverting precious hours from groundbreaking experiments. To address this, we developed a screen-scraping program that automates data collection, allowing us to focus on more critical tasks.

## How do we use it?

Given that our time-of-flight chambers operate under different pressures, simultaneous data collection is essential. This double screen grabber allows users to select specific screen regions displaying these readings, capturing data at approximately 1.5 frames per second per selection. This rate is sufficient for our extended data collection periods, where achieving optimal conditions, such as inducing Cooper pair emission, can be challenging. Each selected area is saved into a separate CSV file, facilitating straightforward analysis and visualization.

## Demo

![Double Screen Grabber Demo](https://github.com/chintanvajariya/double_grabber/assets/49341214/016870be-9e63-4371-b729-512a133b3a0f)

*Note: The demo uses time zone values instead of actual experimental data to maintain confidentiality.*

---

By automating data capture, this tool minimizes manual intervention, thereby reducing errors and freeing up researchers to focus on high-impact activities such as developing ultrafast optical techniques and probing non-equilibrium phenomena in quantum materials. This aligns with our lab's mission to explore and manipulate emergent phases in quantum materials.

## How to Run (macOS Only)

1. **Install dependencies** (preferably in a virtual environment):

    ```bash
    pip install pyautogui pytesseract
    ```

2. **Install Tesseract OCR** (if not already installed):

    On macOS, use Homebrew:

    ```bash
    brew install tesseract
    ```

3. **Run the script**:

    ```bash
    python your_script_name.py
    ```

4. **Follow the prompts**:

    - You’ll be asked to select **two screen regions**.
    - Once selected, the tool will begin logging the text in those regions to two separate `.csv` files, saved with timestamps.

> **Note:** This tool currently supports **macOS only**, due to its use of full-screen transparent overlays that rely on macOS-specific behavior.
