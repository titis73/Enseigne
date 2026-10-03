"""
Classe : Vendeur
Module : enseigne.vendeur
Description : Représente un vendeur au sein d'une enseigne de sport.
"""

from datetime import datetime, timezone

from enseigne.rayon import Rayon


class Vendeur:
    def __init__(
        self,
        nom: str,
        prenom: str,
        tel: str,
        email: str,
        prise_fonction: datetime,
        indice_salaire: int,
        rayon: Rayon,
        cumul_ventes: float = 0.0,
    ) -> None:
        """Constructeur de la classe Vendeur.

        Args:
            nom: Nom du vendeur.
            prenom: Prénom du vendeur.
            tel: Numéro de téléphone du vendeur.
            email: Email du vendeur dans l'enseigne.
            prise_fonction: Moment où le vendeur commence officiellement à exercer son poste.
            indice_salaire: Indice de la grille de salaire.
            rayon: Rayon auquel est assigné le vendeur.
            cumul_ventes: Montant cumulé de ses ventes.
        """
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email
        self.prise_fonction = prise_fonction
        self.indice_salaire = indice_salaire
        self.rayon = rayon
        self.cumul_ventes = cumul_ventes

    def __str__(self) -> str:
        date_formatee = self.prise_fonction.strftime("%d/%m/%Y à %H:%M")
        return (
            f"Vendeur : {self.prenom} {self.nom}\n"
            f"  - Tél : {self.tel}\n"
            f"  - Email : {self.email}\n"
            f"  - Rayon : {self.rayon}\n"
            f"  - Prise de fonction : {date_formatee}\n"
            f"  - Indice de salaire : {self.indice_salaire}\n"
            f"  - Ventes cumulées : {self.cumul_ventes} €"
        )


if __name__ == "__main__":
    r1 = Rayon("VTT")
    v1 = Vendeur(
        prenom="Jean",
        nom="Benguigui",
        tel="0624567267",
        email="Benguigui@gmail.com",
        prise_fonction=datetime.now(tz=timezone.utc),
        rayon=r1,
        indice_salaire=1,
    )
    print(v1)


"""
TODO : Ajouter la relation entre Vendeur et Secteur d'activité quand elle sera créée
"""
