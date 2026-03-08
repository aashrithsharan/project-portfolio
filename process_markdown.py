import re
import os
from pathlib import Path

def remove_hyperlinks(text):
    """Remove hyperlinks and convert them to plain text"""
    # Convert [text](url) to just text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove standalone URLs with http/https
    text = re.sub(r'https?://[^\s\)]+', '[URL_REMOVED]', text)
    return text

def sanitize_content(content, filename):
    """Remove sensitive information from markdown content"""
    
    # Remove all hyperlinks
    content = remove_hyperlinks(content)
    
    # Remove specific sensitive patterns
    sensitive_patterns = {
        # Replace specific production URLs that might have been missed
        'aashrith-enterprise-stack.vercel.app': '[DEPLOYMENT_URL]',
        'enthusiastic-insight-production.up.railway.app': '[API_URL]',
        'localhost:3000': 'localhost:PORT',
        'localhost:8000': 'localhost:PORT',
        'localhost:5000': 'localhost:PORT',
        'localhost:9100': 'localhost:PORT',
        'localhost:9200': 'localhost:PORT',
        # Remove any email-like patterns
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b': '[EMAIL]',
        # Remove API key references
        'GEMINI_API_KEY': 'GEMINI_API_KEY',
        'OPENAI_API_KEY': 'OPENAI_API_KEY',
        'ANTHROPIC_API_KEY': 'ANTHROPIC_API_KEY',
    }
    
    for pattern, replacement in sensitive_patterns.items():
        if pattern.startswith('r\''):
            content = re.sub(pattern, replacement, content)
        else:
            content = content.replace(pattern, replacement)
    
    # Remove [URL_REMOVED] if it appears in code blocks (we want to keep structure)
    # But keep it in prose
    
    return content

def process_markdown_files(directory):
    """Process all markdown files in the directory"""
    path = Path(directory)
    md_files = list(path.glob('*.md'))
    
    print(f"Found {len(md_files)} markdown files to process")
    
    for md_file in md_files:
        print(f"\nProcessing: {md_file.name}")
        
        try:
            # Read the file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Process content
            cleaned_content = sanitize_content(content, md_file.name)
            
            # Write back
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            print(f"✓ Successfully processed {md_file.name}")
            
        except Exception as e:
            print(f"✗ Error processing {md_file.name}: {str(e)}")
    
    print("\n" + "="*50)
    print("Processing complete!")
    print("="*50)

if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    process_markdown_files(script_dir)
