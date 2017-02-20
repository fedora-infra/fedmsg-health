#!/usr/bin/env python
from mako.template import Template
from collections import OrderedDict

timespans = OrderedDict([
    ('now', 900),
    ('hour', 3600),
    ('day', 86400),
    ('week', 604800),
    ('month', 2628000),
    ('year', 365 * 86400),
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
        'consumer': 'CacheInvalidator',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'packages03.phx2.fedoraproject.org',
        'title': 'fedora-packages',
    }, {
        'consumer': 'StatsConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'statscache-backend01.phx2.fedoraproject.org',
        'title': 'statscache',
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
        'consumer': 'Masher',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'bodhi-backend01.phx2.fedoraproject.org',
        'title': 'bodhi-masher',
    }, {
        'consumer': 'UpdatesHandler',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'bodhi-backend02.phx2.fedoraproject.org',
        'title': 'bodhi-updates-handler',
    }, {
        'consumer': 'BugzillaTicketFiler',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'hotness01.phx2.fedoraproject.org',
        'title': 'the-new-hotness',
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
        'host': 'pkgs02.phx2.fedoraproject.org',
        'title': 'genacls',
    }, {
        'consumer': 'SummerShumConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'summershum01.phx2.fedoraproject.org',
        'title': 'summershum',
    }, {
        'consumer': 'KojiConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'fedimg01.phx2.fedoraproject.org',
        'title': 'fedimg (cloud uploader)',
    }, {
        'consumer': 'AutoCloudConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'autocloud-backend-libvirt.phx2.fedoraproject.org',
        'title': 'autocloud-backend-libvirt',
    }, {
        'consumer': 'AutoCloudConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'autocloud-backend-vbox.phx2.fedoraproject.org',
        'title': 'autocloud-backend-vbox',
    }, {
        'consumer': 'BugyouConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'bugyou01.phx2.fedoraproject.org',
        'title': 'bugyou',
    }, {
        'consumer': 'PDCUpdater',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'pdc-backend01.phx2.fedoraproject.org',
        'title': 'pdc-updater',
    }, {
        'consumer': 'FasClientConsumer',
        'instance': 'hub',
        'plugin': 'fedmsg',
        'host': 'batcave01.phx2.fedoraproject.org',
        'title': 'fas_client',
    },
]

if __name__ == '__main__':
    names = timespans.keys()
    for name in names:
        html = Template(filename="template.html").render(
            name=name,
            names=names,
            span=timespans[name],
            parameters=parameters
        )

        with open('build/fedmsg-health-%s.html' % name, 'w') as f:
            f.write(html)

        if name == 'day':
            with open('build/fedmsg-health.html', 'w') as f:
                f.write(html)
