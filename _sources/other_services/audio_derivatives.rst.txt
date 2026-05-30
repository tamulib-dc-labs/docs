===========================================
Audio: Creating Service Files for Streaming
===========================================

Oral history collections present a three-tier file management challenge: preservation masters,
production access copies, and streaming derivatives. This document focuses on the third tier,
the files delivered to end users via a streaming server, and explains the format and encoding
decisions made for that context.

Why Not the Preservation Master?
---------------------------------

Preservation masters from George Blood tend to be Broadcast Wave Format (BWF) files encoded at
96 kHz / 24-bit PCM. These files are intentionally lossless and uncompressed to support
long-term archival integrity. A single 30-minute recording at this specification produces
roughly 1 GB of data. Streaming a file of that size is impractical: it places unnecessary
load on the server, requires the client to buffer an enormous file, and consumes bandwidth
disproportionate to the perceptible quality benefit for a listener using typical headphones
or computer speakers.

Why Not MP3?
------------

George Blood typically provides 192 kbps MP3 access copies. MP3 is a mature, widely supported
format, but it has two shortcomings in this context:

**Acoustic efficiency.** MP3's psychoacoustic model was designed in the early 1990s. For
speech content like oral histories, MP3 is less efficient than modern codecs. A 192 kbps MP3 file occupies roughly
three times the bandwidth needed to deliver equivalent or better perceived quality using a current codec.

**Derivative of a derivative.** These MP3 files were already transcoded from the
preservation masters. Streaming the MP3 as-is is not inherently wrong, but re-encoding
from the master allows control over the output quality and avoids compounding generation
loss if the MP3 itself was ever re-encoded in the future.

Choosing Opus?
--------------

Opus (RFC 6716) is an open, royalty-free codec standardized by the IETF in 2012 and
developed by Xiph.Org and Mozilla. It is the recommended choice for oral histories for
the following reasons:

**Speech optimization.** Opus incorporates the SILK codec (originally developed by Skype
for voice communication) at lower bitrates, making it exceptionally well-suited to speech
content. At 64 kbps, Opus consistently outperforms MP3 at 192 kbps for voice in
perceptual listening tests.

**Efficiency.** At 64 kbps, a 30-minute oral history recording produces approximately
15 MB (about 1.5% of the preservation master's size) with no perceptible quality
loss for the intended use case.

**Open standard.** Opus is royalty-free and unencumbered by software patents, which
is consistent with the values of open-access digital library projects.

**Browser support.** Opus in an Ogg container (``.opus``) is natively supported in all
major modern browsers (Firefox, Chrome, Edge, Safari 17+) without plugins and is streamable
by Kaltura, the streaming platform we use in Avalon.

**Variable bitrate.** The ``-vbr on`` flag we use for processing instructs the encoder to allocate more bits
to acoustically complex passages and fewer to silence or simple tones, improving perceived quality at a given average
bitrate.


Encoding Specification
----------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Parameter
     - Value
   * - Input
     - Preservation master (96 kHz / 24-bit BWF/WAV)
   * - Codec
     - Opus (libopus)
   * - Bitrate
     - 64 kbps (VBR)
   * - Container
     - Ogg (``.opus``)
   * - Channels
     - Stereo (downmix from master if needed)
   * - Sample rate
     - 48 kHz (Opus native; ffmpeg resamples automatically)


Single-File Workflow
--------------------

To encode a single preservation master to Opus using `ffmpeg <https://ffmpeg.org/>`_::

    ffmpeg -i input.wav -c:a libopus -b:a 64k -vbr on output.opus

To verify the output::

    ffprobe output.opus

Expected output will show ``Audio: opus``, ``48000 Hz``, ``stereo``, and a bitrate near
64 kb/s.


Batch Conversion Script
-----------------------

The following Python script recursively walks a directory tree, finds all ``.wav`` files,
and encodes each one to Opus. It mirrors the source directory structure in the output
directory, skips files that have already been encoded, and logs all activity.

.. code-block:: python

    #!/usr/bin/env python3
    """
    wav_to_opus.py
    ==============
    Recursively encode WAV preservation masters to Opus streaming derivatives.

    Usage
    -----
    python wav_to_opus.py --input /path/to/masters --output /path/to/streaming

    Optional flags
    --------------
    --bitrate   Target bitrate in kbps (default: 64)
    --dry-run   Print what would be done without encoding anything
    --workers   Number of parallel encoding jobs (default: 4)
    --log       Path to log file (default: wav_to_opus.log)
    """

    import argparse
    import logging
    import subprocess
    import sys
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from pathlib import Path


    def setup_logging(log_path: str) -> logging.Logger:
        logger = logging.getLogger("wav_to_opus")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s  %(levelname)-8s  %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        return logger


    def encode_file(
        wav_path: Path,
        output_path: Path,
        bitrate: int,
        dry_run: bool,
        logger: logging.Logger,
    ) -> bool:
        """
        Encode a single WAV file to Opus.

        Returns True on success, False on failure.
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_path.exists():
            logger.info("SKIP (already exists): %s", output_path)
            return True

        cmd = [
            "ffmpeg",
            "-y",                        # overwrite without prompting
            "-i", str(wav_path),
            "-c:a", "libopus",
            "-b:a", f"{bitrate}k",
            "-vbr", "on",
            "-loglevel", "error",        # suppress ffmpeg progress noise
            str(output_path),
        ]

        if dry_run:
            logger.info("DRY RUN: %s -> %s", wav_path, output_path)
            return True

        logger.info("ENCODING: %s", wav_path.name)
        try:
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True,
            )
            logger.info("DONE: %s", output_path.name)
            return True
        except subprocess.CalledProcessError as exc:
            logger.error(
                "FAILED: %s\n  ffmpeg stderr: %s",
                wav_path,
                exc.stderr.strip(),
            )
            return False


    def collect_jobs(input_root: Path, output_root: Path) -> list[tuple[Path, Path]]:
        """Return a list of (wav_path, opus_output_path) pairs."""
        jobs = []
        for wav_path in sorted(input_root.rglob("*.wav")):
            relative = wav_path.relative_to(input_root)
            output_path = output_root / relative.with_suffix(".opus")
            jobs.append((wav_path, output_path))
        return jobs


    def main() -> None:
        parser = argparse.ArgumentParser(
            description="Recursively encode WAV masters to Opus streaming derivatives."
        )
        parser.add_argument(
            "--input",
            required=True,
            help="Root directory containing WAV preservation masters.",
        )
        parser.add_argument(
            "--output",
            required=True,
            help="Root directory for Opus output files.",
        )
        parser.add_argument(
            "--bitrate",
            type=int,
            default=64,
            help="Target bitrate in kbps (default: 64).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print planned operations without encoding.",
        )
        parser.add_argument(
            "--workers",
            type=int,
            default=4,
            help="Number of parallel encoding jobs (default: 4).",
        )
        parser.add_argument(
            "--log",
            default="wav_to_opus.log",
            help="Log file path (default: wav_to_opus.log).",
        )
        args = parser.parse_args()

        logger = setup_logging(args.log)

        input_root = Path(args.input).resolve()
        output_root = Path(args.output).resolve()

        if not input_root.is_dir():
            logger.error("Input directory not found: %s", input_root)
            sys.exit(1)

        jobs = collect_jobs(input_root, output_root)

        if not jobs:
            logger.warning("No WAV files found under %s", input_root)
            sys.exit(0)

        logger.info(
            "Found %d WAV file(s). Output root: %s. Bitrate: %dk. Workers: %d.",
            len(jobs),
            output_root,
            args.bitrate,
            args.workers,
        )

        success_count = 0
        failure_count = 0

        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    encode_file,
                    wav_path,
                    opus_path,
                    args.bitrate,
                    args.dry_run,
                    logger,
                ): wav_path
                for wav_path, opus_path in jobs
            }

            for future in as_completed(futures):
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1

        logger.info(
            "Complete. Success: %d  Failed: %d",
            success_count,
            failure_count,
        )

        if failure_count:
            sys.exit(1)


    if __name__ == "__main__":
        main()


Example invocations::

    # Encode all WAV masters, 4 parallel jobs
    python wav_to_opus.py \
        --input /Volumes/digital_project_management/Oral_History \
        --output /Volumes/streaming/Oral_History

    # Preview what would be encoded without touching any files
    python wav_to_opus.py \
        --input /Volumes/digital_project_management/Oral_History \
        --output /Volumes/streaming/Oral_History \
        --dry-run

    # Higher bitrate for music or mixed content, 8 parallel jobs
    python wav_to_opus.py \
        --input /Volumes/digital_project_management/Oral_History \
        --output /Volumes/streaming/Oral_History \
        --bitrate 96 \
        --workers 8 \
        --log encoding_run.log


Directory Structure
-------------------

The script preserves the source directory hierarchy. Given a source tree::

    Oral_History/
    ├── 02_00001/
    │   ├── Thomas_Adair-a_01.wav
    │   └── Thomas_Adair-b_01.wav
    └── 02_00002/
        └── Jane_Doe-a_01.wav

The output tree will be::

    streaming/Oral_History/
    ├── 02_00001/
    │   ├── Thomas_Adair-a_01.opus
    │   └── Thomas_Adair-b_01.opus
    └── 02_00002/
        └── Jane_Doe-a_01.opus


Dependencies
------------

- `ffmpeg <https://ffmpeg.org/>`_ must be installed and available on ``PATH``,
  compiled with ``--enable-libopus``.
- Python 3.9 or later (no third-party packages required).

To verify ffmpeg has Opus support::

    ffmpeg -codecs 2>/dev/null | grep opus

You should see a line containing ``libopus`` in the encoders column.


References
----------

- `RFC 6716 — Definition of the Opus Audio Codec <https://datatracker.ietf.org/doc/html/rfc6716>`_
- `Opus Codec — opus-codec.org <https://opus-codec.org/>`_
- `FFmpeg libopus documentation <https://ffmpeg.org/ffmpeg-codecs.html#libopus>`_
- Voran, S. (2013). *Listening tests for Opus*. Institute for Telecommunication Sciences.