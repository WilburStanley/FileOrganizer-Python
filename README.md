# FileOrganizer-Python 🗂️

**A Python GUI automation tool for intelligent file organization with real-time progress tracking and visual feedback.**

---

![image alt](https://github.com/WilburStanley/FileOrganizer-Python/blob/9b562488bdfdaa1d2f7fa363fd44a6195d867d36/exe-img.png)

## 📋 Features

### **Core Functionality**
- **Category-Based Sorting**: Automatically organizes files into predefined categories (Documents, Images, Audio, Video, Spreadsheets, etc)
- **Date-Based Organization**: Optional date sorting within categories using `YYYY-MM_MonthName` format
- **Real-Time Progress Display**: Live logging with color-coded status messages
- **Batch Processing**: Handles multiple files simultaneously with efficient file operations

### **GUI Features**
- **Dark Mode Interface**: Professional black-themed tkinter GUI
- **Color-Coded Logging**: Visual feedback with categorized message types:
  - ✅ **Success** (Green): Completed operations
  - ❌ **Error** (Red): Operation failures
  - ⚠️ **Warning** (Orange): Skipped files or warnings
  - ℹ️ **Info** (Blue): Processing information
  - 🔸 **Step** (Gold): Process milestones
- **Progress Tracking**: Real-time display of file movements and operations
- **User-Friendly Controls**: Simple browse, organize, and clear log functionality

---

## 🚀 Quick Start

### **Option 1: Using Pre-built EXE (Windows)**
1. Go to the `dist` folder in this repository
2. Download `organize.exe`
3. Run the executable
4. Select folder and organize files instantly

### **Option 2: Running from Source**
```bash
# Clone repository
git clone https://github.com/WilburStanley/FileOrganizer-Python.git
cd FileOrganizer-Python

# Run the application (no dependencies needed)
python organize.py
