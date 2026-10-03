"""
Classe : Rayon
Module : modeles.rayon
Description : Représente un rayon de vente spécifique au sein d'une enseigne de sport.
"""

class Rayon:
    _compteur = 0
    def __init__(self, nom: str) -> None:
        """Constructeur de la classe Rayon.

        Args:
            nom: Nom du rayon (ex: Football, Natation, etc.).
        """
        Rayon._compteur += 1
        self.code_rayon = f"RAY-{Rayon._compteur:03d}"
        self.nom = nom

    def __str__(self) -> str:
        return f"(code_rayon = {self.code_rayon}, nom = {self.nom})"


if __name__ == "__main__":
    r1 = Rayon(nom="VTT")
    r2 = Rayon(nom="VTT")
    print(r1)
    print(r2)
