#!/usr/bin/env python
from mako.template import Template
from collections import OrderedDict

timespans = OrderedDict([
    ('hour', 3600),
    ('day', 86400),
    ('week', 604800),
    ('month', 2628000),
    ('year', 3.15 * 10**7),
])

parameters = [
    {
        'consumer': 'Nommer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'busgateway01.phx2.fedoraproject.org',
        'title': 'datanommer',
    }, {
        'consumer': 'GatewayConsumer',
        'instance': 'gateway',
        'plugin': 'fedmsg',
        'host': 'busgateway01.phx2.fedoraproject.org',
        'title': 'gateway',
    }, {
        'consumer': 'RelayConsumer',
        'instance': 'relay',
        'plugin': 'fedmsg',
        'host': 'busgateway01.phx2.fedoraproject.org',
        'title': 'relay',
    }, {
        'consumer': 'BugzillaConsumer',
        'instance': 'hub',
        'plugin': 'moksha',
        'host': 'bugzilla2fedmsg01.phx2.fedoraproject.org',
        'title': 'bugzilla2fedmsg',
    }, {
        'consumer': 'FMNConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'notifs-backend01.phx2.fedoraproject.org',
        'title': 'FMN',
    }, {
        'consumer': 'FedoraBadgesConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'badges-backend01.phx2.fedoraproject.org',
        'title': 'badges',
    }, {
        'consumer': 'IRCBotConsumer',
        'instance': 'irc',
        'plugin': 'fedmsg',
        'host': 'value01.phx2.fedoraproject.org',
        'title': 'irc',
    }, {
        'consumer': 'GenACLsConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'pkgs01.phx2.fedoraproject.org',
        'title': 'genacls',
    }, {
        'consumer': 'SummerShumConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'summershum01.phx2.fedoraproject.org',
        'title': 'summershum',
    },
]

if __name__ == '__main__':
    names = timespans.keys()
    for name in names:
        with open('build/fedmsg-health-%s.html' % name, 'w') as f:
            f.write(Template(filename="template.html").render(
                name=name,
                names=names,
                span=timespans[name],
                parameters=parameters
            ))
