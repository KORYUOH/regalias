# Copyright 2017 Letla Fox
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from argparse import ArgumentParser

from ._version import __version__
from .generate_japanese_alias import generate_japanese_alias


def run_main():
  argparser = ArgumentParser(
      prog='regalias',
      description='Elonalike Alias Generator',
      allow_abbrev=False)
  argparser.add_argument(
      '--version',
      action='version',
      version='%(prog)s version {version}'.format(version=__version__))
  argparser.add_argument('name', nargs='?', help='seed of alias')

  args = argparser.parse_args()

  alias = generate_japanese_alias(args.name)
  if args.name is not None:
    print(alias, args.name)
  else:
    print(alias)