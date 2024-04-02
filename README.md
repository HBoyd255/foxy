# Foxy

A Firefox launcher that opens firefox on the correct desktop.

This script is used to open firefox on the correct screen. By default firefox
will open new tabs in the most recent firefox instance, even if it exist on a
different virtual desktop. This script fixes this by checking if there is an
instance of firefox open on the current desktop, and if not, adds the
`--new-window` argument to firefox.

Windows will only allow you to set the default browser to an executable, so this
script is called by Foxy.exe, which is a compiled autohotkey script, that calls
a VBS script, which calls the python script. At one point I has it all bundled
into an exe using pyinstaller, but this took too long to run, so I stuck with
the current setup.

The icon used if the firefox logo from 2005-2009, I wanted it to be
distinguishable from the current firefox logo, but still be firefox. I also
prefer it to the current logo.

This script only works on windows, because it is used to fix a windows specific
problem.
