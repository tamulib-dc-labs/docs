========================================================
Renaming Files from Preservation for Technology Services
========================================================

Occasionally, we will get files from Special Collections or Preservation with very long filenames. Even though we bundle
these with SAFCreator before we send to technology services to put online with MAGPIE, the filenames may be long and
they will say they can't open the path.  I think this is some Windows thing that I know nothing about.  To fix, before
you write your SAF, you can copy your files to a flatter structure using something like this:

.. code-block:: python

    import csv
    import shutil
    import os
    import sys
    from pathlib import Path


    def sanitize_filename(filename):
        """Keep only the base filename from a path."""
        return os.path.basename(filename)


    def copy_files_and_update_csv(input_csv, output_csv, destination_dir, source_base_dir=None):
        """
        Copy files from CSV to destination and create updated CSV.

        Args:
            input_csv: Path to input CSV file
            output_csv: Path to output CSV file
            destination_dir: Base destination directory for copied files
            source_base_dir: Optional base directory for source files (if paths are relative)
        """
        # Create destination directory
        dest_path = Path(destination_dir)
        dest_path.mkdir(parents=True, exist_ok=True)

        # Track statistics
        stats = {
            'rows_processed': 0,
            'files_copied': 0,
            'files_missing': 0,
            'errors': []
        }

        # Read input CSV and process
        with open(input_csv, 'r', encoding='utf-8') as infile, \
             open(output_csv, 'w', encoding='utf-8', newline='') as outfile:

            reader = csv.DictReader(infile)

            # Verify 'filename' column exists
            if 'filename' not in reader.fieldnames:
                raise ValueError("CSV must contain a 'filename' column")

            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row_num, row in enumerate(reader, start=1):
                stats['rows_processed'] += 1

                # Get filenames (may be multiple, separated by ' | ')
                filename_field = row['filename']
                filenames = [f.strip() for f in filename_field.split('||')]

                # Create row directory (e.g., row_001, row_002, etc.)
                row_dir = dest_path / f"row_{row_num:03d}"
                row_dir.mkdir(exist_ok=True)

                # Copy each file and collect new paths
                new_filenames = []

                for file_path in filenames:
                    # Determine source path
                    if source_base_dir:
                        source_file = Path(source_base_dir) / file_path
                    else:
                        source_file = Path(file_path)

                    # Get the base filename
                    base_name = source_file.name

                    # Destination path
                    dest_file = row_dir / base_name

                    # Copy file
                    try:
                        if source_file.exists():
                            shutil.copy2(source_file, dest_file)
                            stats['files_copied'] += 1
                            print(f"Copied: {source_file} -> {dest_file}")
                        else:
                            stats['files_missing'] += 1
                            error_msg = f"Row {row_num}: File not found: {source_file}"
                            stats['errors'].append(error_msg)
                            print(f"WARNING: {error_msg}")
                            # Still add to new_filenames to preserve structure

                    except Exception as e:
                        error_msg = f"Row {row_num}: Error copying {source_file}: {str(e)}"
                        stats['errors'].append(error_msg)
                        print(f"ERROR: {error_msg}")

                    # Build new relative path
                    new_path = f"{row_dir.name}/{base_name}"
                    new_filenames.append(new_path)

                # Update the filename field with new paths
                row['filename'] = '||'.join(new_filenames)

                # Write updated row to output CSV
                writer.writerow(row)

        return stats


    def main():
        """Main entry point for the script."""
        import argparse

        parser = argparse.ArgumentParser(
            description='Reorganize files from CSV into sequential directories'
        )
        parser.add_argument('-i', '--input_csv', help='Input CSV file')
        parser.add_argument('-d', '--destination_dir', help='Destination directory for copied files')
        parser.add_argument(
            '-o', '--output-csv',
            help='Output CSV file (default: <input>_updated.csv)'
        )
        parser.add_argument(
            '-s', '--source-base',
            help='Base directory for source files (if CSV paths are relative)'
        )

        args = parser.parse_args()

        # Set default output CSV name if not provided
        if not args.output_csv:
            input_path = Path(args.input_csv)
            args.output_csv = input_path.stem + '_updated.csv'

        print(f"Input CSV: {args.input_csv}")
        print(f"Output CSV: {args.output_csv}")
        print(f"Destination: {args.destination_dir}")
        if args.source_base:
            print(f"Source base: {args.source_base}")
        print("-" * 60)

        # Process files
        try:
            stats = copy_files_and_update_csv(
                args.input_csv,
                args.output_csv,
                args.destination_dir,
                args.source_base
            )

            # Print summary
            print("-" * 60)
            print("SUMMARY:")
            print(f"  Rows processed: {stats['rows_processed']}")
            print(f"  Files copied: {stats['files_copied']}")
            print(f"  Files missing: {stats['files_missing']}")
            print(f"  Errors: {len(stats['errors'])}")

            if stats['errors']:
                print("\nErrors encountered:")
                for error in stats['errors'][:10]:  # Show first 10 errors
                    print(f"  - {error}")
                if len(stats['errors']) > 10:
                    print(f"  ... and {len(stats['errors']) - 10} more errors")

            print(f"\nUpdated CSV written to: {args.output_csv}")

        except Exception as e:
            print(f"FATAL ERROR: {e}", file=sys.stderr)
            sys.exit(1)


    if __name__ == '__main__':
        main()


This requires an input csv with a filename column with each file separated like :code:`||`.  Because you might run this from anywhere,
I also suggest that the CSV have the full static path to each file -- not a relative path.  Finally give it an output csv and a directory it
can write to. Your full command will look like this:

.. code-block:: shell

    python reorganize_csv_files.py -i mcinnis.csv -d /Volumes/digital_project_management/mark_playground/mcinnis_new -o mcinnis_new.csv
