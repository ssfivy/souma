# souma
Securely dump system information for later inspection.

## Features
- Dumps various system information in one go

## Use cases
- Devices with sensitive information that needs encrypted debug logs
- Devices installed standalone / remote location
- Devices without central monitoring server
- Devices behind firewalls / airgaps
- Python practice for me!

## TODOs - done
- grab data from systemd journal and write to dump file
- add command to extract dump file

## TODOs
- add metadata to dump file
- extract code into library
- add unit tests
- add CI / CD for tests
- perform above work in chunks
- compress data in chunks
- add checksums in chunks
- Extract tarfile carefully: Handle zip bombs!
- verify checksums during extraction
- add type annotations
- add documentations / readthedocs
- add encryption
- add requirements.txt
- add pip publishing
- add binary signing
- record system information exposed by python standard libraries
- add mechanism to handle different operating systems
- record basic unique information from ubuntu, fedora, yocto, windows (to test above mechanism)
- record essential files from /proc and /sys
- record essential files from /etc
- record information from other filesystem locations
- allow adding list of custom files
- allow adding list of custom commands
- allow adding list of custom metadata
- grab data from other syslog daemons
- allow configuring things at dumping time (e.g. length of syslog to dump)
- add web interface - apache
- add web interface - nginx
- add udev rules example to dump to usb stick / sd card
- add cron job example for regular dumping
- make yocto meta-layer for inclusion
- Write a gui interface for dumping / reading dumps
- gui on windows
- standalone gui packaging
- windows CI/CD using Appveyor (has Python & Qt) or Azure Pipelines
- add resource limit during operation: https://docs.python.org/3.6/library/resource.html
- support alternate compression algorithm (lzma / lz4 / zstd)
- allow extracting only part of syslog
- add to debian / fedora repositories?
- daemon mode that runs constantly and create dumps on demand?
