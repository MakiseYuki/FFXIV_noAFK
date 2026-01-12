# FFXIV NoAFK Project

## Project Structure

```
FFXIV_noAFK/
├── ffxiv_noafk.py          # Main script
├── config.py               # Configuration file
├── requirements.txt        # Python dependencies
├── run.bat                 # Windows batch launcher
└── README.md              # Documentation
```

## Quick Start

1. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

2. **Launch FFXIV game**

3. **Run the script**:
   ```powershell
   python ffxiv_noafk.py
   ```
   
   Or simply double-click `run.bat`

4. **Stop with** `Ctrl+C`

## Customization

Edit `config.py` to change:
- Jump interval (default: 10 minutes)
- Variance/randomness (default: ±2 minutes)
- Game window title
- Key to press
- Logging options

## Logs

All actions are logged to `noafk.log` for verification.
