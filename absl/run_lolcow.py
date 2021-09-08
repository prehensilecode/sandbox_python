#!/usr/bin/env python
from absl import app
from absl import flags
from spython.main import Client
from pathlib import Path
import json

debug = False

FLAGS = flags.FLAGS
flags.DEFINE_string("name", None, "Your name.")
flags.DEFINE_integer("num_times", 1,
                     "Number of times to print greeting.")

def main(argv):
    del argv  # Unused.

    img_path = Path('./lolcow_latest.sif')
    if not img_path or not img_path.is_file():
        Client.pull('library://sylabsed/examples/lolcow:latest', name='lolcow_latest.sif')
    print('Inspect:')
    inspect_json = Client.inspect(img_path, json=True)
    print(json.dumps(inspect_json, indent=4))
    print('')

    myinstance = Client.instance('lolcow_latest.sif')

    if debug:
        print(myinstance.cmd)

    ### the environ keyword parameter is passed to subprocess.popen(env=environ)
    ### - it's a dict {VARNAME: value}
    Client.run(myinstance)

    cowtext = Client.execute(myinstance, ["env"], environ={'FOO': 'bar'})
    print(cowtext)
    cowtext = Client.execute(myinstance, ["cowsay", "hello"])
    print(cowtext)

    ologs = myinstance.output_logs()
    elogs = myinstance.error_logs()

    if ologs:
        print('Output:')
        print(ologs)

    if elogs:
        print('Error:')
        print(elogs)

    # Clean up all instances
    Client.instance_stopall()



if __name__ == '__main__':
    app.run(main)
