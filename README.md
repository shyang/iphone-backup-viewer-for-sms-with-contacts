iPhone Backup Viewer for SMS with Contacts
==========================================

Prerequisites

  * python3
  * sqlite3
  * Mako (pip install Mako)

Configure

  * On Mac, the default iTunes backup folder is located at ~/Library/Application Support/MobileSync/Backup/ (http://support.apple.com/kb/HT4946)
  * Change the path in viewer.py to one subfolder (a long hash with optional timestamp) inside it. (view one backup a time)
    
Run

  * $ ./server.py
  * Open a browser and navigate to http://127.0.0.1:9000

