__author__ = 'fedoseev.ns'

import noc.sa.profiles
from noc.sa.protocols.sae_pb2 import HTTP

class Profile(noc.sa.profiles.Profile):
    name="Harmonic.ProStream1000"
    supported_schemes=[HTTP]