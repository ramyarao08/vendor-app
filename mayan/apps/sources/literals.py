from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

SCANNER_SOURCE_FLATBED = 'flatbed'
SCANNER_SOURCE_ADF = 'Automatic Document Feeder'

SCANNER_SOURCE_CHOICES = (
    (SCANNER_SOURCE_FLATBED, _('Flatbed')),
    (SCANNER_SOURCE_ADF, _('Document feeder')),
)

SCANNER_ADF_MODE_SIMPLEX = 'simplex'
SCANNER_ADF_MODE_DUPLEX = 'duplex'

SCANNER_ADF_MODE_CHOICES = (
    (SCANNER_ADF_MODE_SIMPLEX, _('Simplex')),
    (SCANNER_ADF_MODE_DUPLEX, _('Duplex')),
)

SCANNER_MODE_LINEART = 'lineart'
SCANNER_MODE_MONOCHROME = 'monochrome'
SCANNER_MODE_COLOR = 'color'

SCANNER_MODE_CHOICES = (
    (SCANNER_MODE_LINEART, _('Lineart')),
    (SCANNER_MODE_MONOCHROME, _('Monochrome')),
    (SCANNER_MODE_COLOR, _('Color'))
)

SOURCE_UNCOMPRESS_CHOICE_Y = 'y'
SOURCE_UNCOMPRESS_CHOICE_N = 'n'
SOURCE_UNCOMPRESS_CHOICE_ASK = 'a'

SOURCE_UNCOMPRESS_CHOICES = (
    (SOURCE_UNCOMPRESS_CHOICE_Y, _('Always')),
    (SOURCE_UNCOMPRESS_CHOICE_N, _('Never')),
)

SOURCE_INTERACTIVE_UNCOMPRESS_CHOICES = (
    (SOURCE_UNCOMPRESS_CHOICE_Y, _('Always')),
    (SOURCE_UNCOMPRESS_CHOICE_N, _('Never')),
    (SOURCE_UNCOMPRESS_CHOICE_ASK, _('Ask user'))
)

SOURCE_CHOICE_WEB_FORM = 'webform'
SOURCE_CHOICE_STAGING = 'staging'
SOURCE_CHOICE_WATCH = 'watch'
SOURCE_CHOICE_EMAIL_POP3 = 'pop3'
SOURCE_CHOICE_EMAIL_IMAP = 'imap'
SOURCE_CHOICE_SANE_SCANNER = 'sane'

SOURCE_CHOICES = (
    (SOURCE_CHOICE_SANE_SCANNER, _('Scanner')),
    (SOURCE_CHOICE_WEB_FORM, _('Web form')),
    (SOURCE_CHOICE_STAGING, _('Staging folder')),
    (SOURCE_CHOICE_WATCH, _('Watch folder')),
    (SOURCE_CHOICE_EMAIL_POP3, _('POP3 email')),
    (SOURCE_CHOICE_EMAIL_IMAP, _('IMAP email')),
)

DEFAULT_INTERVAL = 600
DEFAULT_METADATA_ATTACHMENT_NAME = 'metadata.yaml'
DEFAULT_POP3_TIMEOUT = 60
DEFAULT_IMAP_MAILBOX = 'INBOX'
DEFAULT_SOURCE_TASK_RETRY_DELAY = 10

# Upload wizard steps
STEP_DOCUMENT_TYPE = '0'
STEP_METADATA = '1'
STEP_TAGS = '2'
