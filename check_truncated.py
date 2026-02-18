import os
import sys

INDICATORS = [
    '```',           # fenced code blocks suggest truncation happened
    '| ',            # tables that might have been cut
]

def check_file(filepath):
    """Check if a markdown file appears truncated."""
    issues = []
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Check 1: File ends abruptly (no trailing newline or ends mid-sentence)
    last_meaningful = ''
    for line in reversed(lines):
        if line.strip():
            last_meaningful = line.strip()
            break
    
    if last_meaningful and not last_meaningful.endswith(('.', '?', '!', ':', '*', '`', '-', '|')):
        issues.append(f"  Ends abruptly: ...{last_meaningful[-60:]}")
    
    # Check 2: Has opening ## section headers — check last one has content
    headers = [(i, line) for i, line in enumerate(lines) if line.startswith('#')]
    if headers:
        last_header_idx = headers[-1][0]
        content_after = ''.join(lines[last_header_idx + 1:]).strip()
        if len(content_after) < 20:
            issues.append(f"  Last section nearly empty: {headers[-1][1]}")
    
    # Check 3: Very short file (likely truncated)
    if len(content) < 500:
        issues.append(f"  Very short: {len(content)} chars")
    
    # Check 4: Has fenced code blocks (would have caused truncation)
    fence_count = content.count('```')
    if fence_count > 0:
        issues.append(f"  Contains {fence_count} backtick fences (may have survived or may indicate partial content)")
    
    # Check 5: Unmatched fences
    if fence_count % 2 != 0:
        issues.append(f"  ODD number of fences ({fence_count}) — likely truncated mid-block")
    
    # Check 6: Expected sections missing — check for "Open Questions" or "Key Works"
    has_open_questions = 'Open Questions' in content
    has_key_works = 'Key Works' in content or 'Key Sources' in content or 'Key References' in content
    if not has_open_questions and not has_key_works:
        issues.append(f"  Missing both 'Open Questions' and 'Key Works/Sources' sections")
    elif not has_open_questions:
        issues.append(f"  Missing 'Open Questions' section")
    
    return issues


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    truncated = []
    clean = []
    
    for dirpath, _, filenames in sorted(os.walk(root)):
        for fname in sorted(filenames):
            if not fname.endswith('.md'):
                continue
            if fname == 'README.md':
                continue
            
            filepath = os.path.join(dirpath, fname)
            relpath = os.path.relpath(filepath, root)
            issues = check_file(filepath)
            
            if issues:
                truncated.append((relpath, issues))
            else:
                clean.append(relpath)
    
    if truncated:
        print(f"⚠️  {len(truncated)} file(s) may be truncated:\n")
        for relpath, issues in truncated:
            print(f"  {relpath}")
            for issue in issues:
                print(f"    {issue}")
            print()
    
    if clean:
        print(f"✅ {len(clean)} file(s) look complete:\n")
        for relpath in clean:
            print(f"  {relpath}")
    
    print(f"\nTotal: {len(truncated)} suspect, {len(clean)} clean")


if __name__ == '__main__':
    main()