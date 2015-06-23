; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "PyPlane"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "Institut fuer Regelungs- und Steuerungstheorie"
!define PRODUCT_WEB_SITE "https://github.com/TUD-RST/pyplane.git"

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME

; Directory page
!insertmacro MUI_PAGE_DIRECTORY

; Instfiles page
!insertmacro MUI_PAGE_INSTFILES

; Finish page
!insertmacro MUI_PAGE_FINISH

; Language files
!insertmacro MUI_LANGUAGE "English"

; MUI end ------

RequestExecutionLevel user

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "windows\build\PyPlane_Setup.exe"
InstallDir "$DESKTOP\PyPlane"
ShowInstDetails show

Section "Hauptgruppe" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File /r "windows\build\PyPlane\*"
  CreateShortCut "$DESKTOP\PyPlane.lnk" "$INSTDIR\PyPlane.exe"
SectionEnd