# Die Funktionen von dem Bot erklärt

Dieser Python Code implementiert ein Nextcord Bot mit verschiedenen Slash Commands, um Moderationsaufgaben in einem Discord Server auszuführen. Der Bot verwendet die Nextcord Bibliothek und die commands Erweiterung von Nextcord, um die Befehle zu erstellen.

Zunächst wird der Bot erstellt und der Discord Server, auf dem der Bot agieren soll, wird festgelegt.

Es gibt eine Slash Command Group:
- `moderation`: Er dient als Überkategorie für die Moderations Commands

Es gibt vier Slash Commands:

- `ban`: Dieser Command bannt einen Nutzer und sendet eine Bestätigungsnachricht an den Moderator und eine Benachrichtigungsnachricht an den gebannten Nutzer.
- `kick`: Dieser Command kickt einen Nutzer und sendet eine Bestätigungsnachricht an den Moderator und eine Benachrichtigungsnachricht an den gekickten Nutzer.
- `notice`: Dieser Command erstellt einen Thread in einem bestimmten Channel mit einer Notiz, die vom Moderator erstellt wurde.
- `whisper`: Dieser Command sendet eine private Nachricht von einem Moderator an einen Nutzer.
