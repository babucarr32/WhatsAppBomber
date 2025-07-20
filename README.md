# 💣 WhatsApp Message Bomber (Educational Tool)

This is an educational Python tool that automates sending repeated messages to a WhatsApp Web contact using **Selenium WebDriver**.

> ⚠️ **Disclaimer**: This tool is for **educational purposes only**. The author is not responsible for any misuse or damage caused by this script.

---

## 🚀 Features

- Launches WhatsApp Web with your Chrome profile.
- Prompts for the full XPath of a target chat.
- Sends custom messages repeatedly to the selected contact.
- Works on **Windows**, **Linux**, and **macOS**.
- Styled CLI output with color-coded messages and ASCII banner.

---

## 📦 Requirements

- Python 3.8+
- Google Chrome
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (placed in a `/driver/` directory)
- [ChromeDriver JSON](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json) (Download from here)

---

## 📁 Folder Structure

```
your-project/
├── WhatsAppBomberBanner.py
├── config.py
├── WhatsAppBomber.py
├── driver/
│   └── chromedriver / chromedriver.exe
```

---

## ⚙️ Setup

1. **Install Dependencies**:

   ```bash
   pip install selenium
   ```

2. **Set Chrome Profile Path**:

   Update `config.py` with your Chrome profile path:

   ```python
   CHROME_PROFILE_PATH = "--user-data-dir=/path/to/your/chrome/profile"
   ```

   Example:

   ```python
   CHROME_PROFILE_PATH = "--user-data-dir=/Users/you/Library/Application Support/Google/Chrome"
   ```

3. **Ensure ChromeDriver is Present**:

   Download the correct version of ChromeDriver for your system and place it in the `driver/` folder:

   - `driver/chromedriver` (Linux/macOS)
   - `driver/chromedriver.exe` (Windows)

---

## 🛠 Usage

Run the tool:

```bash
python main.py
```

1. Scan the QR code in the launched browser (if not already authenticated).
2. Enter the full XPath to your target chat (right-click > Inspect > Copy XPath).
3. Confirm the target.
4. Enter the message and number of times to send it.

**Example Usage**:

```
Enter target Full XPath: /html/body/div[1]/div/div/div[3]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/span/span
Please confirm the target (yes/no): yes
Enter message to send: Hello from bot
Enter amount: 10
```

---

## ⚠️ Disclaimer

This tool is intended for testing and educational purposes only.

Do not use it to harass or spam others.

The author takes no responsibility for misuse of this software---

## 👤 Author

Baboucarr Badjie
