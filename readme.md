## XDefaults to Putty color configuration converter

For all you windows customization lovers out there who have a taste for beautiful looking terminals, you probably know it's a pretty big pain to setup the colors in putty. Fortunately the colors for a putty session are easily stored in the windows registry so we can use a `.reg` file to add a predefined set of terminal colors for a putty session.

Using this tool you can convert a standard Xdefaults (Xresources) file that includes terminal colors into a registry file to set the colors to a putty session!

### Usage

To use this converter simply run it as `./convert .Xdefaults PuttySessionName1 PuttySessionName2 ...` > colors.reg

You can specify multiple putty sessions. A putty session is the name of a stored session in the putty client configuration.