#!/usr/bin/env python3
import sys
import os
from absl import app
from absl import flags
from spython.main import Client
from pathlib import Path
import json

# Couldn't get path binds to work using instances.
# Also, couldn't start an instance specifying a path bind. 
# XXX If I understand correctly, instance(..., **kwargs) should be passed to
# the start() method, but it didn't like getting a list of tuples.
# From https://github.com/singularityhub/singularity-cli/blob/130366c5e1aba58d7746db39b434f34a1e5fcdd2/spython/instance/cmd/start.py
# Correction: it wants a list of strings, see: https://singularityhub.github.io/singularity-cli/commands-images#execute
# it looks like it just wants the commandline option in a string, 
# and start() does a split(" ")

FLAGS = flags.FLAGS
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')
flags.DEFINE_bool('use_gpu', True, 'Enable NVIDIA runtime to run with GPUs.')
flags.DEFINE_string('bind', None, 'Path bind specification.')

def main(argv):
    del argv  # Unused.

    img_path = Path('./lolcow_latest.sif')
    if not img_path or not img_path.is_file():
        Client.pull('library://sylabsed/examples/lolcow:latest', name='lolcow_latest.sif')
    myimg = Client.load(str(img_path))
    print('Inspect:')
    inspect_json = Client.inspect(myimg, json=True)
    print(json.dumps(inspect_json, indent=4))
    print('')

    if FLAGS.debug:
        print(f'DEBUG: type(myimg) = {type(myimg)}')
        print(f'DEBUG: myimg = {myimg}')

    print('Using Client.run(myimg)')
    Client.run(myimg)
    print('')

    # Client.execute() starts a transient instance: the instance
    # culls itself once the execution is done.

    tmpdir = os.environ['TMPDIR']

    print('Using Client.execute(myimg, ...)')
    if FLAGS.use_gpu:
        cowtext = Client.execute(myimg, ["ls", "-ld", "/fakedata"], environ={'FOO': 'bar'}, bind=[f'{tmpdir}:/mnt', f'{tmpdir}/fakedata:/fakedata'], options=['--nv'] if FLAGS.use_gpu else None)
        #cowtext = Client.execute(myimg, ["env"], environ={'FOO': 'bar'}, bind=[f'{tmpdir}:/mnt'], options=['--nv'])
        print(cowtext)
        print('')
        cowtext = Client.execute(myimg, ["ls", "-l", "/mnt"], environ={'FOO': 'bar'}, bind=[f'{tmpdir}:/mnt'], options=['--nv'] if FLAGS.use_gpu else None)
        print(cowtext)
        print('')
        cowtext = Client.execute(myimg, ["nvidia-smi"], environ={'FOO': 'bar'}, bind=f'{tmpdir}:/mnt', options=['--nv'] if FLAGS.use_gpu else None)
        print(cowtext)
        print('')
        cowtext = Client.execute(myimg, ["/mnt/external_runscript.sh"], environ={'FOO': 'bar'}, bind=f'{tmpdir}:/mnt', options=['--nv'] if FLAGS.use_gpu else None)
        print(cowtext)
        print('')
    else:
        cowtext = Client.execute(myimg, ["env"], environ={'FOO': 'bar'}, bind=f'{os.environ["TMPDIR"]}:/mnt')
        print(cowtext)
        print('')
        cowtext = Client.execute(myimg, ["ls", "-l", "/mnt"], environ={'FOO': 'bar'}, bind=f'{os.environ["TMPDIR"]}:/mnt')
        print(cowtext)
        print('')
        cowtext = Client.execute(myimg, ["/mnt/external_runscript.sh"], environ={'FOO': 'bar'}, bind=f'{os.environ["TMPDIR"]}:/mnt')
        print(cowtext)
        print('')



if __name__ == '__main__':
    app.run(main)
