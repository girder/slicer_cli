import os
import pytest
from pytest_girder.web_client import runWebClientTest


@pytest.mark.plugin('sclicer_cli_web')
@pytest.mark.parametrize('spec', (
    'parseSpec.js',
    'widgetSpec.js',
))
def testWebClient(boundServer, fsAssetstore, db, spec):  # noqa
    spec = os.path.join(os.path.dirname(__file__), 'web_client_specs', spec)
    runWebClientTest(boundServer, spec, 15000)
