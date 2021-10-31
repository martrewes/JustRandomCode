# Now playing applet for Quodlibet / XFCE

Just a simple applet thrown together in Python to display the currently playing song from Quodlibet in the XFCE Panel.

## Howto use
>Requires the GenMon applet:
>### Arch based distros:
>`sudo pacman -S xfce4-genmon-plugin`
>### Debian based:
>`sudo apt install xfce4-genmon-plugin`
>### Fedora based:
>`sudo dnf install xfce-genmon-plugin`

Once installed point the Generic Monitor applet to the script:
`/usr/bin/python [script/location]`

## Screenshot
![img](Screenshot.png)

## Additional Cover Art
I have modified the default `write_cover.py` plugin to resize the cover so it also fits on my XFCE taskbar. 

Place the `cover_mod.py` file in `/usr/lib/python3.9/site-packages/quodlibet/etc/events` (requires root). Then create another genmon applet and set the command to `echo "<img>/home/username/.config/quodlibet/cover.jpg<\img>`

![img](Screenshot2.png)