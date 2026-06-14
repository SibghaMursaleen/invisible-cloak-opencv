<h1 align="center">🧥 Invisible Cloak — OpenCV</h1>

<p align="center">
  A real-time <strong>Harry Potter–inspired invisibility cloak</strong> effect built with Python and OpenCV.<br/>
  Wear a black cloth, step in front of your webcam, and watch yourself disappear.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-1.x-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

---

## 📌 Overview

This project recreates the **Invisibility Cloak** effect from the Harry Potter universe using real-time computer vision. It works by capturing a static background image, then replacing any detected cloak-colored pixels in subsequent frames with the corresponding region from that background — making the cloth appear transparent.

> **Default cloak color:** Black &nbsp;|&nbsp; **Alternate support:** Red (commented in code)

---

## ⚙️ How It Works

The pipeline runs through five stages on every captured frame:

| Step | Stage | Description |
|------|-------|-------------|
| 1 | **Background Capture** | A clean background frame is saved before the subject enters the scene |
| 2 | **Color Detection** | Frame is converted to HSV; a color mask isolates the target cloak color |
| 3 | **Mask Refinement** | Morphological `OPEN` + `DILATE` operations remove noise and smooth edges |
| 4 | **Layer Separation** | Frame is split into the cloak region and the non-cloak region |
| 5 | **Compositing** | Cloak region is swapped with background pixels; layers are merged via `addWeighted` |

---

## 📁 Project Structure

```
invisible-cloak-opencv/
│
├── webcam.py          # Step 1 — Launches webcam and captures the background image
├── test_webcam.py     # Step 2 — Runs the live real-time invisibility effect
├── .gitignore         # Excludes background.jpg and Python artifacts
└── README.md
```

> **Note:** `background.jpg` is **not included** in this repository. It is generated locally by running `webcam.py` and must be present before running `test_webcam.py`.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A working webcam

Install the required dependencies:

```bash
pip install opencv-python numpy
```

---

### Step 1 — Capture Your Background

Stand **completely out of the camera frame**, then run:

```bash
python webcam.py
```

| Key | Action |
|-----|--------|
| `c` | Capture and save `background.jpg` |
| `q` | Quit without capturing |

The script saves `background.jpg` in the project directory and closes automatically after capture.

---

### Step 2 — Run the Cloak Effect

Once the background is saved, put on your **black cloth** and run:

```bash
python test_webcam.py
```

| Key | Action |
|-----|--------|
| `q` | Quit the effect |

The cloak region is replaced in real-time with the saved background, creating the invisibility illusion.

---

## 🎨 Cloak Color Configuration

Open `test_webcam.py` to switch cloak colors:

| Color | HSV Range | Status |
|-------|-----------|--------|
| ⬛ Black | `[0,0,0]` → `[180,255,50]` | ✅ Active |
| 🔴 Red | `[0,100,50]` → `[15,255,255]` + `[165,100,50]` → `[180,255,255]` | 💬 Commented out |

To enable red, comment out the black mask block and uncomment the red mask block in `test_webcam.py`.

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **Python 3** | Core programming language |
| **OpenCV** | Webcam capture, HSV conversion, morphological ops, rendering |
| **NumPy** | Array manipulation and HSV threshold arrays |

---

## ⚠️ Tips for Best Results

- **Lighting matters** — Use consistent, bright lighting to get a clean background capture.
- **Static camera** — Do not move the camera between capturing the background and running the effect.
- **Solid-colored cloth** — A uniform black cloth with no patterns produces the cleanest mask.
- **Cloak fully in frame** — The HSV range is tuned for pure black; very dark navy may also trigger the mask.

---

## 📄 License

This project is released under the [MIT License](LICENSE) — free to use, modify, and distribute for educational and personal purposes.

---

<p align="center">
  Built with 🐍 Python + 👁️ OpenCV &nbsp;·&nbsp; Inspired by the wizarding world of Harry Potter
</p>
