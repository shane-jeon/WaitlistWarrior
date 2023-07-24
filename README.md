# Waitlist Warrior

This mischevious yet sophisticated project leverages the power of Selenium, Python, Beautiful Soup, and Twilio to implement a robust notification system. The system continously monitors the class availability on MindBody, a popular booking platform, and promptly alerts users when a class that was previously marked as "_full_" transitions to either "_waitlist_" or "_book_" status.

Gone are the days of manually checking the class availabilty multiple times throughout the day. With this automated solution, you can now focus on securing a spot in your desired classes at your pole studio (or any studio come future developments) without any hassle. The integration of Selenium WebDriver facilitates seamless web scraping, while Beautiful Soup skillfully parses the extracted data for real-time updates.

Through Twilio's cutitng-edge SMS notification capabilities, you will receive instant text message notificaitons when the status changes, ensuring you stay ahead of the game and never miss an opportunity to join your preferred class.

Join us in revolutionizing the way you book your pole studio classes by integrating this advanced MindBody Class Status Notifier, **Waitlist Warrior**, into your workflow. Enhance your class booking experience and seize the chance to take your passion for pole to new heights!

Stay tuned for future updates~~
Features:

Installation:

Contribute:

Support:

License:

NOTES TO SELF:

## Setup

### Selecting appropriate ChromeDriver

- Beginning by installing chromedriver
  - check current version of chrome by selecting Chrome --> About Google Chrome
  - For example: I have Google Chrome version 115. If you also have the most updated version of Chrome, click on following link to download the current ChromeDriver (115 is durrently a Chrome for Testing version, though the channel is "Stable"). [ChromeDriver v.115](https://googlechromelabs.github.io/chrome-for-testing/#stable). Select the driver depending on your OS.
    - [ChromeDriver](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.102/mac-arm64/chrome-mac-arm64.zip) for Mac devices w/Apple M1
    - [ChromeDriver](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.102/mac-x64/chrome-mac-x64.zip) for Mac devices w/Intel
    - Unfortunately I have personally not worked with Linux or Windows, but the following [link](https://googlechromelabs.github.io/chrome-for-testing/#stable) will take you to a page providing JSON endpoints for specific ChromeDriver versions.
  - If you have Google Chrome v.114 or below, click following link to download older ChromeDriver versions [ChromeDriver v.114 & below](https://googlechromelabs.github.io/chrome-for-testing/#stable)

### ChromeDriver Installation

1. _Once download is complete_, open the ZIP file and extract the WebDriver. It is best to place the WebDriver to a location on your MAC in a directory that is included in your system's PATH variable
2. _Move Chrome WebDriver to suitable directory_:

- Find location in which you would like to place the WebDriver. Copy WebDriver path.
- Open the Terminal. _For macOS version before Catalina (macOS 10.15) users only_ --> you will need to edit the bash profile to use the default zsh shell.
  - Enter following commands:
    - `open ~/.zshrc`
    - Ensure following `PATH` variable is set in your `~/.zshrc` file. If missing, add to file. `export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"`
    - Add following line to end of `~/.zshrc` file to include the Chrome WebDriver path:
      `export PATH="/Users/[insert path to webdriver]/chromedriver:$PATH"`
    - Save `~/.zshrc` file and close TextEditor.
    - Apply changes to current Terminal session by running `source ~/.zshrc`
    - Verify WebDriver installation by running `chromedriver --version`. If it returns in error, try following `/Users/[insert path to chromedriver]/chromedriver --version`
      - If a window pops up stating "ChromeDriver cannot be opened because developer cannot be verified" resolve issue by following steps below:
        **Allow the execution of the ChromeDriver**
        1. Locate ChromeDriver executable in its' directory
        2. Right click `chromedriver` file
        3. Choose "Open" from context menu
        4. Upon seeing a warning message stating that the developer cannot be verified, Click "Open" again to confirm.

### Create Environment & Install Requirements

1. Create virtual environment `python3 -m venv .venv`
2. Activate virtual environment `source .venv/bin/activate`
3. Install requirements with following command `pip3 install -r requirements.txt`
