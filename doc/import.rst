################################
Risikoeinschätzungen importieren
################################

Wenn schon Risikoeinschätzungen z.B. im Excel-Format vorhanden sind, können diese über einen CSV-Datei importiert werden. Für folgende Attribute der Multivaluekategorie "Risikoeinschätzung" wurden aufgrund der Komplexität eigene Importmethoden geschrieben:

**Auswirkung / Auswirkung nach Risikobehandlung**
    Hier muss eine Semikolon-getrennte Liste an Schadensauswirkungen angegeben werden. Für jedes Schadensszenarium wird dafür das Level als Zahl eingegeben, sortiert nach dem Attribut "Kennzeichnung" aus der Kategorie "Schadensszenario". 
    Beispiel: Sie haben vier Bewertungskriterien definiert mit den Leveln 1 bis 4. Des Weiteren haben Sie drei Schadensszenarien definiert: 

    * "Finanzielle Auswirkungen" mit der Kennzeichnung "1"
    * "Persönliche Unversehrtheit" mit der Kennzeichnung "2"
    * "Verstoß gegen Verträge/Gesetze" mit der Kennzeichnung "3"

    Sie wollen nun bei einer Risikoeinschätzung folgende Werte für die Schadensauswirkung der drei Schadensszenarien importieren:

    * Finanzielle Auswirkungen: Level 4 
    * Persönliche Auswirkung: Level 1
    * Verstoß gegen Verträge/Gesetze: Level 2

    Dann muss der zu importierende Wert so aussehen: 4;1;2

**Existierende Maßnahmen / Maßnahmen zur Risikobehandlung**
    Hier muss jeweils eine Semikolon-getrennte Liste der SOA-Maßnahmen angegeben werden. Dabei kann sowohl der Objekttitel als auch die Objekt-ID zur Identifizierung der SOA-Maßnahme angegeben werden. Sollte im Titel ein Semikolon vorkommen, muss dieses mit einem Backslash escaped werden.

    Um die SOA-Maßnahmen "Aufstellung von Handfeuerlöschern" (ID 2985) und "Installation einer Brandmeldeanlage" (ID 3054) an der Risikoeinschätzung zu importieren, wären folgene Varianten möglich:

    * Aufstellung von Handfeuerlöschern;Installation einer Brandmeldeanlage
    * 2985;3054
    * Aufstellung von Handfeuerlöschern;3054
    * 2985;Installation einer Brandmeldeanlage

Alle anderen Attribute der Multivaluekategorie "Risikoeinschätzung" können in der Standardsyntax von i-doit importiert werden.


.. |pfeil| unicode:: U+23F5