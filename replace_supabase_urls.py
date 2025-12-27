#!/usr/bin/env python3
"""
Script om Supabase project URLs te vervangen in index.html
"""

import re
import sys

def replace_supabase_urls(project_id, file_path='index.html'):
    """
    Vervangt alle instanties van YOUR_SUPABASE_PROJECT met de daadwerkelijke project ID
    
    Args:
        project_id: Je Supabase project ID (bijv. 'abcdefghijklmnop')
        file_path: Pad naar het HTML bestand (standaard: index.html)
    """
    try:
        # Lees het HTML bestand
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tel hoeveel instanties er zijn
        count = content.count('YOUR_SUPABASE_PROJECT')
        
        if count == 0:
            print(f"Geen instanties van 'YOUR_SUPABASE_PROJECT' gevonden in {file_path}")
            return False
        
        # Vervang alle instanties
        content = content.replace('YOUR_SUPABASE_PROJECT', project_id)
        
        # Schrijf terug
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {count} instanties vervangen met project ID: {project_id}")
        print(f"✓ Bestand opgeslagen: {file_path}")
        return True
        
    except FileNotFoundError:
        print(f"✗ Fout: Bestand '{file_path}' niet gevonden")
        return False
    except Exception as e:
        print(f"✗ Fout: {str(e)}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Gebruik: python replace_supabase_urls.py <SUPABASE_PROJECT_ID>")
        print("\nVoorbeeld:")
        print("  python replace_supabase_urls.py abcdefghijklmnop")
        print("\nOf pas de SUPABASE_PROJECT_ID hieronder aan en run het script:")
        sys.exit(1)
    
    project_id = sys.argv[1]
    
    # Optioneel: specificeer een ander bestand
    file_path = sys.argv[2] if len(sys.argv) > 2 else 'index.html'
    
    success = replace_supabase_urls(project_id, file_path)
    
    if success:
        print("\n✓ Klaar! Controleer index.html om te verifiëren dat alle URLs correct zijn.")
    else:
        sys.exit(1)

