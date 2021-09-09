#!/bin/bash
singularity exec --bind $TMPDIR:/mnt lolcow_latest.sif ls -l /mnt
singularity exec --bind $TMPDIR:/mnt lolcow_latest.sif /mnt/external_runscript.sh
