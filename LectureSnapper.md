# LectureSnapper 📸

Extract unique slides from video lectures and convert them into a single PDF automatically!

## ✨ Features

- 🎨 **Modern Dark UI**: Built with CustomTkinter for a sleek, professional appearance
- 🎯 **Smart Detection**: Uses Structural Similarity Index (SSIM) to detect slide changes
- 🎚️ **Adjustable Sensitivity**: Interactive slider (0.70-0.95) to control detection sensitivity
- 📊 **Real-time Progress Bar**: See exactly how much of your video has been processed
- ⚡ **Fast Processing**: Optimized frame comparison with intelligent downscaling
- 📁 **Batch Processing**: Select and process multiple videos at once
- 🚫 **Sleep Prevention**: Automatically prevents screen saver/sleep during processing
- 📄 **PDF Output**: Compiles all unique slides into a single PDF document
- 🎨 **User-Friendly**: Simple file picker interface with live status updates
- 🧹 **Auto Cleanup**: Removes temporary files after processing
- 🧵 **Non-blocking UI**: Processing runs in separate thread - GUI stays responsive
- ⏸️ **Pause/Resume**: Pause processing at any time and resume when ready
- 🛑 **Cancellation**: Stop processing immediately if needed

## 🖥️ Screenshots

The app features a modern dark theme with:
- Clean, intuitive interface
- Real-time progress tracking
- Interactive sensitivity control
- Live status log with color-coded messages

## 📦 Installation

1. Make sure Python 3.8+ is installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Simply run:
```bash
python lecture_snapper.py
```

Or use the desktop shortcut for one-click access!

### Step-by-Step:

1. **Launch** the application (double-click desktop shortcut)
2. **Adjust sensitivity** using the slider if needed:
   - Lower values (0.70-0.80): Captures more slides, more sensitive to changes
   - Higher values (0.85-0.95): Captures fewer slides, only major changes
3. **Select video files** using the "Select Video Files" button
   - You can select multiple files at once for batch processing
   - Use "Clear List" to remove files from the queue
4. **Click "Start Processing"** and watch the progress bar
5. **Control processing** with Pause/Resume/Cancel buttons as needed:
   - ⏸️ **Pause**: Temporarily pause processing
   - ▶️ **Resume**: Continue after pausing
   - 🛑 **Cancel**: Stop processing completely
6. **Wait for completion** - your laptop won't sleep during processing!
7. **Get your PDFs** - success popup shows how many files were processed

### 🎛️ Configuration

Edit these variables in `lecture_snapper.py` to customize behavior:

- `DEFAULT_SIMILARITY_THRESHOLD` (0.70-0.95): Default sensitivity
  - Lower (e.g., 0.75): Detects smaller changes
  - Higher (e.g., 0.90): Only detects major changes
  - Default: 0.85
  - **Can be adjusted in GUI with slider!**

- `SAMPLE_INTERVAL_SECONDS`: Time between frame checks
  - Lower: More accurate but slower
  - Higher: Faster but might miss quick changes
  - Default: 1.5 seconds

## 📤 Output

The PDF will be saved in the same directory as your video file with the suffix `_slides.pdf`.

Example: `lecture_video.mp4` → `lecture_video_slides.pdf`

## ⚡ Performance

Processing speed depends on video length and resolution:

- **30-minute video**: ~1-2 minutes
- **60-minute video**: ~2-4 minutes
- **2-hour video**: ~4-8 minutes

The app shows real-time progress so you always know how long is left!

## 🛠️ Technical Details

- **GUI Framework**: CustomTkinter (modern, themed UI)
- **Video Processing**: OpenCV (cv2)
- **Similarity Detection**: Scikit-image SSIM algorithm
- **PDF Generation**: img2pdf
- **Threading**: Asynchronous video processing for responsive UI
- **System Integration**: Prevents sleep/screensaver during processing

## 📋 Requirements

- Python 3.8+
- opencv-python
- scikit-image
- img2pdf
- numpy
- customtkinter
- darkdetect

See `requirements.txt` for specific versions.

## 🎓 Use Cases

Perfect for:
- 📚 Students recording online lectures
- 👨‍🏫 Educators creating study materials
- 💼 Professionals capturing presentation slides
- 🎥 Anyone who wants to extract slides from videos

## 🐛 Troubleshooting

**App not opening?**
- Make sure Python and all dependencies are installed
- Try running from terminal: `python lecture_snapper.py`

**Processing too slow?**
- Increase `SAMPLE_INTERVAL_SECONDS` to 2 or 3
- Close other heavy applications

**Too many/few slides detected?**
- Adjust the sensitivity slider in the GUI
- Lower values = more slides
- Higher values = fewer slides

**Laptop went to sleep?**
- This should no longer happen! The app now prevents sleep during processing
- If it still occurs, check your power settings

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Feel free to open issues or submit pull requests on GitHub!

---

Created with ❤️ for students and educators

## 📌 Version History

**Version 2.2** (December 28, 2025)
- ➕ Added batch processing for multiple videos
- ➕ Added scrollable file list display
- ➕ Added "Clear List" button
- ⚡ Optimized processing speed with intelligent frame downscaling
- 🎨 Enhanced UI for multiple file selection

**Version 2.1** (December 28, 2025)
- ➕ Added Pause/Resume functionality
- ➕ Added Cancel button to stop processing
- 🎨 Enhanced UI with control buttons
- 🔧 Improved button state management

**Version 2.0** (CustomTkinter Edition)
- 🎨 Complete UI redesign with CustomTkinter
- 📊 Added real-time progress bar
- 🎚️ Interactive sensitivity slider
- 🚫 Sleep prevention during processing
