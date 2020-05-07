#############################
Objekttyp Informationsverbund
#############################

.. image:: img/scope_100x100.jpg
     :class: floatright

Für jeden Informationsverbund gibt es genau ein Objekt vom Typ "Informationsverbund". In der Regel gibt es also nur ein Objekt vom Typ Informationsverbund, das VIVA2-Addon bietet aber auch die Möglichkeit, mehrere Informationsverbünde zu dokumentieren. In der Standardkonfiguration gehören folgende Kategorien zu Objekten vom Typ Informationsverbund:

**Allgemein** *(i-doit Standardkategorie)* 
    Gehört zu jedem Objekt.
**IT-Grundschutz (Informationsverbund)** 
    Dies ist eine Kategorien-Gruppe, die die folgenden vier Kategorien beinhaltet:
    
    **Informationsverbund**
        Hier werden die grundlegenden Informationen zum Informationsverbund dokumentiert wie der bereinigte Netzplan und die Leitlinie zur Informationssicherheit
    **Infrastrukturanalyse**
        Diese Multivalue-Kategorie zeigt alle mit diesem Informationsverbund über die rückwärtige Kategorie "Informationsverbünde" direkt verknüpften Objekte an. Mehr dazu findet man unter :doc:`strukturanalyse`.
    **IT-Grundschutz-Check**
        Die Übersichtsseite zeigt alle durch die Bausteine zugewiesenen Anforderungen, sortiert nach Baustein und Anforderungsnummer. Mehr dazu findet man unter :doc:`it-grundschutz-check`.
    **Prozessbausteine**
        Hier können die Prozessbausteine zugewiesen werden, die für den gesamten Informationsverbund gelten. Aus technischer Sicht können auch  Systembausteine zugewiesen werden, in der Regel werden diese jedoch den jeweiligen Zielobjekten bzw. Zielobjektgruppen zugewiesen. Mehr dazu findet man unter :doc:`strukturanalyse`.
**Kontaktzuweisung** *(i-doit Standardkategorie)* 
    Hier müssen die entsprechenden Rollen für den kompletten Informationsverbund eingetragen werden, allen voran natürlich der Informationssicherheitsbeauftraget (ISB).
**Report: Anwendungen ohne Installation**
    Dieser variable Report zeigt alle Anwendungen an, die auf keiner Maschine installiert sind (laut Dokumentation in i-doit). Es werden alle Anwendungen überprüft, die entweder direkt diesem Informationsverbund zugeordnet sind oder die Mitglieder einer Zielobjektgruppe sind, die diesem Informationsverbund zugeordnet ist.
**Report: IT-Grundschutz-Check**
    Dieser variable Report zeigt alle Anforderungen und deren Umsetzungsstatus an, die über Bausteine diesem Informationsverbund zugeordnet sind. Es werden dabei nicht nur die Anforderungen aus den direkt zugewiesenen Bausteinen berücksichtigt, sondern auch die aus den Bausteinen, die den zugewiesenen Zielobjekten/Zielobjektgruppen zugewiesen sind.
**Report: Physische Hardware ohne Standort**
    Dieser variable Report zeigt alle Objekte an, denen die Kategorie "Standort" zugewiesen ist, diese aber nicht gepflegt ist. Es werden alle Objekte überprüft, die entweder direkt diesem Informationsverbund zugeordnet sind oder die Mitglieder einer Zielobjektgruppe sind, die diesem Informationsverbund zugeordnet ist.
**Report: Räume ohne Gebäude**
    Dieser variable Report zeigt alle Räume an, bei denen die Standortkategorie nicht gepflegt ist oder bei denen das Standortobjekt keine Adresse eingetragen hat. Es werden alle Räume überprüft, die entweder direkt diesem Informationsverbund zugeordnet sind oder die Mitglieder einer Zielobjektgruppe sind, die diesem Informationsverbund zugeordnet ist.
**Report: Räume ohne Raumnummer**
    Dieser variable Report zeigt alle Räume an, bei denen keine Raumnummer eingetragen ist. Es werden alle Räume überprüft, die entweder direkt diesem Informationsverbund zugeordnet sind oder die Mitglieder einer Zielobjektgruppe sind, die diesem Informationsverbund zugeordnet ist.
**Report: Vom Informationsverbund abgedeckt**
    Dieser variable Report zeigt alle Objekte an, die entweder direkt diesem Informationsverbund zugeordnet sind oder die Mitglieder einer Zielobjektgruppe sind, die diesem Informationsverbund zugeordnet ist.