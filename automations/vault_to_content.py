import os
import shutil
import frontmatter
import re

# --- CONFIGURATION ---
# The absolute path to your Obsidian vault
OBSIDIAN_PATH = r"C:\Users\eminm\Emin's Vault"
# The absolute path to your Quartz content folder
QUARTZ_PATH = r'C:\Users\eminm\digitalgarden\content'
# The folder within your Quartz content folder to store attachments
ATTACHMENTS_SUBFOLDER = 'attachments'
# --- END CONFIGURATION ---

def should_publish(note_path):
    """Checks if a note has `publish: true` or `publish: 1` in its frontmatter."""
    if not os.path.exists(note_path):
        return False
    with open(note_path, 'r', encoding='utf-8') as f:
        try:
            metadata = frontmatter.load(f).metadata
            publish_flag = metadata.get('publish')
            return publish_flag == 1 or publish_flag == True
        except Exception as e:
            # Handles files with no frontmatter
            return False

def find_file_path(file_name, search_root):
    """Finds the full path of a file in a directory tree, returning the first match."""
    for root, dirs, files in os.walk(search_root):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# --- NEW FUNCTION: Delete conflict files ---
def delete_conflict_notes():
    print("Deleting notes with 'conflict' in filename...")
    deleted_count = 0
    for root, dirs, files in os.walk(OBSIDIAN_PATH):
        if '.obsidian' in dirs:
            dirs.remove('.obsidian')
        for file in files:
            if file.endswith('.md') and 'conflict' in file.lower():
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"  - Deleted: {file_path}")
                deleted_count += 1
    print(f"Deleted {deleted_count} conflict files.\n")

def sync_files():
    """
    Synchronizes published notes and their attachments from an Obsidian vault
    to a Quartz content folder.
    """
    QUARTZ_ATTACHMENTS_PATH = os.path.join(QUARTZ_PATH, ATTACHMENTS_SUBFOLDER)
    os.makedirs(QUARTZ_ATTACHMENTS_PATH, exist_ok=True)

    published_notes = set()
    required_attachments = set()
    total_md_files = 0

    # Step 0: Delete conflict notes before anything else
    delete_conflict_notes()

    # Step 1: Scan Obsidian vault
    print("Scanning Obsidian vault...")
    for root, dirs, files in os.walk(OBSIDIAN_PATH):
        if '.obsidian' in dirs:
            dirs.remove('.obsidian')

        for file in files:
            if file.endswith('.md'):
                total_md_files += 1
                note_path = os.path.join(root, file)
                if should_publish(note_path):
                    published_notes.add(file)
                    with open(note_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        image_refs = re.findall(r'!\[\[(.*?)\]\]|!\[.*?\]\((.*?)\)', content)
                        for ref in image_refs:
                            attachment_path = next((item for item in ref if item), None)
                            if attachment_path:
                                attachment_name = os.path.basename(attachment_path.replace("/", os.sep))
                                required_attachments.add(attachment_name)

    print(f"Found {len(published_notes)} published notes and {len(required_attachments)} required attachments.")

    # Step 2: Sync notes
    print("\nSyncing notes...")
    copied_notes_count = 0
    for note_file in published_notes:
        obsidian_note_path = find_file_path(note_file, OBSIDIAN_PATH)
        if obsidian_note_path:
            quartz_note_path = os.path.join(QUARTZ_PATH, note_file)
            if not os.path.exists(quartz_note_path) or \
               os.path.getmtime(obsidian_note_path) > os.path.getmtime(quartz_note_path):
                shutil.copy2(obsidian_note_path, quartz_note_path)
                print(f"  - Copied/Updated note: {note_file}")
                copied_notes_count += 1

    # Step 3: Sync attachments
    print("\nSyncing attachments...")
    copied_attachments_count = 0
    for attachment_name in required_attachments:
        obsidian_attachment_path = find_file_path(attachment_name, OBSIDIAN_PATH)
        if obsidian_attachment_path:
            quartz_attachment_path = os.path.join(QUARTZ_ATTACHMENTS_PATH, attachment_name)
            if not os.path.exists(quartz_attachment_path) or \
               os.path.getmtime(obsidian_attachment_path) > os.path.getmtime(quartz_attachment_path):
                shutil.copy2(obsidian_attachment_path, quartz_attachment_path)
                print(f"  - Copied/Updated attachment: {attachment_name}")
                copied_attachments_count += 1
        else:
            print(f"  - WARNING: Attachment not found in vault: {attachment_name}")

    # Step 4: Clean up notes in Quartz
    print("\nCleaning up old files...")
    deleted_notes_count = 0
    for file in os.listdir(QUARTZ_PATH):
        if file.endswith('.md') and file not in published_notes:
            os.remove(os.path.join(QUARTZ_PATH, file))
            print(f"  - Deleted note: {file}")
            deleted_notes_count += 1

    # Step 5: Clean up unused attachments
    deleted_attachments_count = 0
    if os.path.exists(QUARTZ_ATTACHMENTS_PATH):
        for file in os.listdir(QUARTZ_ATTACHMENTS_PATH):
            if file not in required_attachments:
                os.remove(os.path.join(QUARTZ_ATTACHMENTS_PATH, file))
                print(f"  - Deleted attachment: {file}")
                deleted_attachments_count += 1

    # --- Summary ---
    print("\n--- Sync Summary ---")
    print(f"Total markdown files in vault: {total_md_files}")
    print(f"Notes synced: {copied_notes_count}")
    print(f"Notes deleted: {deleted_notes_count}")
    print(f"Attachments synced: {copied_attachments_count}")
    print(f"Attachments deleted: {deleted_attachments_count}")
    print("--------------------")


if __name__ == '__main__':
    sync_files()
