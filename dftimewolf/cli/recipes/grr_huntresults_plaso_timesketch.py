# -*- coding: utf-8 -*-
"""Download the results of a GRR hunt and process them.

- Collect results of a hunt given its Hunt ID
- Processes results with a local install of plaso
- Exports processed items to a new Timesketch sketch
"""
from __future__ import unicode_literals

_short_description = ('Fetches the findings of a GRR hunt, processes them with '
                      'plaso, and sends the results to Timesketch.')

contents = {
    'name':
        'grr_huntresults_plaso_timesketch',
    'short_description': _short_description,
    'modules': [{
        'wants': [],
        'name': 'GRRHuntDownloader',
        'args': {
            'hunt_id': '@hunt_id',
            'grr_server_url': '@grr_server_url',
            'grr_username': '@grr_username',
            'grr_password': '@grr_password',
            'reason': '@reason',
            'approvers': '@approvers',
            'verify': '@verify',
        },
    }, {
        'wants': ['GRRHuntDownloader'],
        'name': 'LocalPlasoProcessor',
        'args': {
            'timezone': None,
        },
    }, {
        'wants': ['LocalPlasoProcessor'],
        'name': 'TimesketchExporter',
        'args': {
            'endpoint': '@ts_endpoint',
            'username': '@ts_username',
            'password': '@ts_password',
            'incident_id': '@reason',
            'sketch_id': '@sketch_id',
        }
    }],
}

args = [
    ('hunt_id', 'ID of GRR Hunt results to fetch', None),
    ('reason', 'Reason for exporting hunt (used for Timesketch description)',
     None),
    ('--sketch_id', 'Sketch to which the timeline should be added', None),
    ('--approvers', 'Emails for GRR approval request', None),
    ('--grr_server_url', 'GRR endpoint', 'http://localhost:8000'),
    ('--verify', 'Whether to verify the GRR TLS certificate', True),
    ('--grr_username', 'GRR username', 'admin'),
    ('--grr_password', 'GRR password', 'admin'),
]
