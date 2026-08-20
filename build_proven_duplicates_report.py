from pathlib import Path
import json
from collections import defaultdict

root = Path('/home/ubuntu/autobahnhub/audits')
inv = json.loads((root/'mapping_listing_inventory.json').read_text())
vehicles = inv['vehicles']

# Critère strict et irréfutable de doublon artificiel :
# Deux annonces sont des doublons stricts si elles ont EXACTEMENT la même signature technique complète ET la même image principale (URL Unsplash exacte ou même hash de visuel).
# Cela protège les véhicules légitimement similaires (qui partagent un modèle mais ont des kilométrages, prix ou images différents).

seen = {}
duplicates = []
kept = []

for v in vehicles:
    price_val = v.get('priceEur') if v.get('priceEur') is not None else v.get('price', 0)
    sig = (
        v['brand'].strip().lower(),
        v['model'].strip().lower(),
        v['year'],
        v['mileage'],
        price_val,
        v['mainImage'].strip()
    )
    
    if sig in seen:
        duplicates.append({
            'duplicateId': v['id'],
            'originalId': seen[sig],
            'brand': v['brand'],
            'model': v['model'],
            'year': v['year'],
            'mileage': v['mileage'],
            'price': price_val,
            'mainImage': v['mainImage'],
            'proof': f"Doublon strict prouvé : identique à l'annonce ID {seen[sig]} en marque, modèle, année, kilométrage, prix et URL d'image principale."
        })
    else:
        seen[sig] = v['id']
        kept.append(v)

report = {
    'totalListingsBefore': len(vehicles),
    'listingsToKeep': len(kept),
    'listingsProposedForRemoval': len(duplicates),
    'duplicatesProposed': duplicates
}

(root/'proven_duplicates_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

md = [
    '# Rapport d’audit non destructif — Doublons stricts prouvés',
    '',
    '**Statut : Aucune suppression n’a été effectuée.** Ce rapport présente l’inventaire certifié des doublons stricts identifiés parmi les 362 annonces en croisant l’ensemble des critères (marque, modèle, année, kilométrage, prix et image principale).',
    '',
    '## Synthèse',
    '',
    '| Indicateur | Valeur |',
    '|---|---:|',
    f'| Nombre total d’annonces audité | **{len(vehicles)}** |',
    f'| Annonces uniques légitimes conservées | **{len(kept)}** |',
    f'| **Doublons stricts et artificiels prouvés proposés à la suppression** | **{len(duplicates)}** |',
    '',
    '## Liste détaillée des IDs proposés à la suppression',
    '',
    'Puisque chaque critère (spécifications techniques et image) doit correspondre rigoureusement à une autre annonce existante pour qu’il s’agisse d’une copie artificielle, voici le résultat du contrôle :',
    ''
]

if not duplicates:
    md.append('> **Aucun doublon strict combinant exactement les mêmes spécifications techniques ET la même image principale n’a été trouvé parmi les 362 annonces.** Les annonces du catalogue possèdent toutes soit des identifiants, soit des prix, soit des kilométrages, soit des images distincts qui les différencient en tant qu’entrées individuelles. Aucune suppression n’est requise sur la base d’un doublon d’image/spécification croisé.')
else:
    md.append('| ID doublon | ID original | Marque | Modèle | Année | Kilométrage | Prix | Preuve de duplication |')
    md.append('|---:|---:|---|---|---:|---:|---:|---|')
    for d in duplicates:
        md.append(f"| {d['duplicateId']} | {d['originalId']} | {d['brand']} | {d['model']} | {d['year']} | {d['mileage']} km | €{d['price']} | {d['proof']} |")

md += [
    '',
    '## Prochaine étape',
    '',
    'Le catalogue a été audité de manière exhaustive et non destructive. En attente de vos instructions pour approuver ou refuser toute action future.',
    ''
]

(root/'proven_duplicates_report.md').write_text('\n'.join(md)+'\n', encoding='utf-8')
print(json.dumps({'total': len(vehicles), 'toKeep': len(kept), 'toRemove': len(duplicates)}, ensure_ascii=False, indent=2))
