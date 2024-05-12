[Setup]
AppName=BongoKeyboardWidget
AppVersion=1.0
DefaultDirName={pf}\BongoKeyboardWidget
DefaultGroupName=BongoKeyboardWidget
UninstallDisplayIcon={app}\YourAppIcon.ico
Compression=lzma2/ultra
OutputDir=Output
OutputBaseFilename=BongoKeyboardWidgetSetup

[Files]
Source: "dist\main.exe"; DestDir: "{app}"
Source: "1.gif"; DestDir: "{app}"
Source: "2.gif"; DestDir: "{app}"

[Icons]
Name: "{group}\BongoKeyboardWidget"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,BongoKeyboardWidget}"; Flags: nowait postinstall shellexec
