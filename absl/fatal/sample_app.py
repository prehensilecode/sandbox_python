# Copyright 2017 The Abseil Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test helper for smoke_test.sh."""

import sys

from absl import app
from absl import flags
from absl import logging

FLAGS = flags.FLAGS

flags.DEFINE_string('echo', None, 'Text to echo.')


def main(argv):
    del argv  # Unused.

    print('Running under Python {0[0]}.{0[1]}.{0[2]}'.format(sys.version_info), 
          file=sys.stderr)
    logging.info('echo is %s.', FLAGS.echo)

    DOFAIL = True
    if DOFAIL:
        logging.fatal(f'DOFAIL = {DOFAIL} - this app should terminate now')


if __name__ == '__main__':
    app.run(main)
