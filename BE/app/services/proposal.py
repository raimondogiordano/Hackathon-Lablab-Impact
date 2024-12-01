from app.models.schemas.main import QuartiereProposal
from typing import List


def generate_labels(row) -> List[str]:
    labels = []
    if row.get('1B_persone') and row.get('1B_persone').lower() != "card integrata":
        labels.append('Inclusione Sociale')
    if row.get('2B_piccoli') and row.get('2B_piccoli').lower() != "card integrata":
        labels.append('Supporto ai Bambini')
    if row.get('3B_verde') and row.get('3B_verde').lower() != "card integrata":
        labels.append('Spazi Verdi')
    if row.get('4B_sicura') and row.get('4B_sicura').lower() != "card integrata":
        labels.append('Sicurezza')
    if row.get('5B_pulita') and row.get('5B_pulita').lower() != "card integrata":
        labels.append('Pulizia Urbana')
    if row.get('6B_insieme') and row.get('6B_insieme').lower() != "card integrata":
        labels.append('Coesione Sociale')
    if row.get('7B_rigener') and row.get('7B_rigener').lower() != "card integrata":
        labels.append('Rigenerazione Urbana')
    if row.get('8B_vicina') and row.get('8B_vicina').lower() != "card integrata":
        labels.append('Prossimità ai Servizi')
    if row.get('9B_cultura') and row.get('9B_cultura').lower() != "card integrata":
        labels.append('Promozione Culturale')
    if row.get('10B_social') and row.get('10B_social').lower() != "card integrata":
        labels.append('Iniziative Sociali')
    if row.get('11B_clima') and row.get('11B_clima').lower() != "card integrata":
        labels.append('Sostenibilità Climatica')
    if row.get('12B_conosc') and row.get('12B_conosc').lower() != "card integrata":
        labels.append('Conoscenza e Informazione')
    return labels

# Function to convert a row from the DataFrame into a QuartiereProposal instance
def row_to_proposal(row) -> QuartiereProposal:
    # Concatenate all fields starting with 'b_' into a single string for the proposal field, filtering out None, placeholder values, and duplicates
    proposal_fields = [
        row.get('1B_persone'),
        row.get('2B_piccoli'),
        row.get('3B_verde'),
        row.get('4B_sicura'),
        row.get('5B_pulita'),
        row.get('6B_insieme'),
        row.get('7B_rigener'),
        row.get('8B_vicina'),
        row.get('9B_cultura'),
        row.get('10B_social'),
        row.get('11B_clima'),
        row.get('12B_conosc'),
    ]
    # Remove None, placeholder values, and keep unique values only
    filtered_proposal_fields = list(dict.fromkeys(filter(lambda x: x and x.lower() != "card integrata", proposal_fields)))
    proposal_text = " \n".join(filtered_proposal_fields)

    proposal = QuartiereProposal(
        geo_point=row['Geo Point'],
        geo_shape=row['Geo Shape'],
        nome=row['Nome'],
        quartiere=row['Quartiere'],
        zona_prossimita=row['zona di prossimità'],
        proposal=proposal_text
    )
    proposal.labels = generate_labels(row)
    return proposal