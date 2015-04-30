# Android Mouse Cursor

An (sort-of functional) example of how you can simulate a moouse on Android using a floating window and an Accessbility Service to click on Views.

## Usage

- Open the project in Android Studio and run on your device.
- Go to Settings > Accessibility and turn on "MouseCursor".
- Edit the IP address in `mouse_udp_client.py` to that of your Android device
- Run `mouse_udp_client.py` and use the instructions on screen to send mouse events to the service running on the device

## Limitations

- What you click on must be identified as an Accessibility Element. Most basic native apps work, but more complex apps (e.g. Google Maps, games) will not be fully clickable.
- The system UI is inaccessible to floating window used to draw the mouse cursor and the click mechanism. This means you cannot click on the Home or Back buttons or the status bar.
- Dragging the mouse is not supported.
- Right/middle click are not supported.

## Licence

MIT

