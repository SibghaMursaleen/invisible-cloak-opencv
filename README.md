# 🧥 Invisible Cloth — OpenCV

> A Harry Potter–inspired **Invisible Cloak** effect built with Python and OpenCV.  
> Point your webcam at yourself wearing a **black cloth**, and watch it vanish — replaced by the background behind you.

---

## ✨ How It Works

The effect is achieved through classic **computer vision** techniques:

1. **Capture the background** — A clean shot of the scene without you in it.
2. **Detect the cloak color** — Each live frame is converted to HSV color space, and a color mask isolates the target color (black by default).
3. **Mask refinement** — Morphological operations (`OPEN` + `DILATE`) clean up noise and smooth mask edges.
4. **Blend the layers** — The masked cloak region is replaced with the corresponding area from the saved background, while the rest of the frame remains unchanged.
5. **Output** — The two layers are combined using `cv2.addWeighted` to produce the final "invisible" effect.

---

## 📁 Project Structure

```
Invisible Cloth - OpenCV/
│
├── webcam.py          # Step 1 — Captures and saves the background image
├── test_webcam.py     # Step 2 — Runs the live invisible cloak effect
└── README.md
```

> ⚠️ **`background.jpg` is not included in this repo.**  
> You must generate it yourself using `webcam.py` before running the effect.

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python 3.x installed, then install the required libraries:

```bash
pip install opencv-python numpy
```

### 2. Capture Your Background

Run `webcam.py` first. Stand **out of frame**, then press **`c`** to capture and save the background:

```bash
python webcam.py
```

- Press **`c`** → Captures and saves `background.jpg` in the project folder
- Press **`q`** → Quit without capturing

### 3. Run the Invisible Cloak

Once `background.jpg` is saved, run the main script:

```bash
python test_webcam.py
```

- Wear a **black cloth** and step in front of the camera
- Press **`q`** to quit

---

## 🎨 Cloak Color Support

The project currently detects **black** as the cloak color.  
A **red cloak** variant is included in the code as commented-out blocks — simply uncomment those lines in `test_webcam.py` to switch.

| Color  | Status             |
|--------|--------------------|
| ⬛ Black | ✅ Active (default) |
| 🔴 Red  | 💬 Commented out   |

---

## 🛠️ Tech Stack

| Tool       | Purpose                            |
|------------|------------------------------------|
| Python 3   | Core language                      |
| OpenCV     | Webcam capture, masking, rendering |
| NumPy      | Array operations & HSV masking     |

---

## 📸 Demo

> Run `webcam.py`, capture your background, then run `test_webcam.py` while wearing a black cloth.  
> The cloth region is replaced in real-time with the saved background — creating the illusion of invisibility.

---

## 📄 License

This project is open-source and free to use for learning and experimentation.
