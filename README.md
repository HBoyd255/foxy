# Foxy

A Firefox launcher that opens Firefox on the correct desktop.

This script is used to open Firefox on the correct screen. By default, Firefox
will open new tabs in the most recent Firefox instance, even if it exists on a
different virtual desktop. This script fixes this by checking if there is an
instance of Firefox open on the current desktop, and if not, adds the
`--new-window` argument to Firefox.

Windows will only allow you to set the default browser to an executable, so this
script is called by foxy.exe, which is a compiled AutoHotkey script, that calls
the Python script. At one point I had it all bundled into an exe using
pyinstaller, but this took too long to run, so I stuck with the current setup.

The icon used if the Firefox logo from 2005-2009, I wanted it to be
distinguishable from the current Firefox logo, but still be Firefox. I also
prefer it to the current logo.

This script only works on Windows because it is used to fix a Windows specific
problem.

## Dependencies

To run the script, you need Python, which can be downloaded from
[python.org](https://www.python.org/). The following Python libraries are
required:

- `pyvda`
- `psutil`

To compile the exe, you need AutoHotkey, which can be downloaded from
[AutoHotkey.com](https://www.autohotkey.com/).

## How to use

- Clone or download this repository to a desired location. You should decide on
  the final location of this repository before you proceed because if you set
  an app as a default app, then move it, it leaves ghosts.
- To compile the script, right click on `foxy.ahk`and
  select`Compile script (GUI)`. Select the icon you want and press compile.
- Change the value of `FIREFOX_DIRECTORY` in main.py if Firefox in installed in
  a location different to `C:\\Program Files\\Mozilla Firefox`.
- In Windows settings, go to Apps > Default apps, search for Firefox, for each
  entry select `Choose an app on your PC` and select `foxy.exe`.
- after compiling, foxy.exe and main.py are required to be kept in the same
  directory.
- If you use Wox, the plugins `Browser Bookmarks`, `URL` and `Web search` all
  work with foxy.exe To set this up, in Wox settings, select each of these
  plugins, next to `Please set your browser path:` press `Choose` and then find
  foxy.exe. Make sure to set `Open bookmark in:` to `New tab` otherwise it will
  not work properly.

## Removing ghosts

If you decide to move foxy.exe, you may need to do some steps to remove the
ghosts left in the default apps menu, I used Default Programs Editor, which can
be downloaded at [defaultprogramseditor.com](http://defaultprogramseditor.com).
