#!/usr/bin/env python
#-*- coding:utf-8 -*-
#-*- hack2me.com website -*-
#-*- author:younger.shen -*-

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# location index methods

import os
import web
from jinja2 import Environment, PackageLoader
import app
import main
from utils.tools import jinja
from utils.tools import host_addr

class index:
    def GET(self):
        template = jinja.get_template('index.html')
        return template.render(host_addr = host_addr)

    def POST(self):
        return 'test'
class Main:
    def GET(self):
        return test
