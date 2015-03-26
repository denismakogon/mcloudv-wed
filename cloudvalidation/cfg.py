#    Copyright 2015 Mirantis, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
from oslo_config import cfg


dashboard_settings = [
    cfg.StrOpt("dashboard_host", default="0.0.0.0"),
    cfg.IntOpt("dashboard_port", default="8877")
]

rest_client_opts = [
    cfg.StrOpt("cloudv_host",
               default=os.environ.get("MCLOUDV_HOST", "localhost")),
    cfg.IntOpt("cloudv_port",
               default=os.environ.get("MCLOUDV_PORT", 8777)),
    cfg.StrOpt("cloudv_api_version",
               default=os.environ.get("MCLOUDV_API", "v1"))
]

CONF = cfg.CONF
CONF.register_opts(dashboard_settings)
CONF.register_opts(rest_client_opts)


def parse_args(argv, default_config_files=None):
    cfg.CONF(args=argv[1:],
             project='cloudvalidation-web',
             version="1.0",
             default_config_files=default_config_files)
