#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


class UploadParam:
    def __init__(self, file="", head=1, partition=10,
                 namespace="", name="", work_mode=0, storage_engine="", storage_address=None, destroy=False):
        self.file = file
        self.head = head
        self.partition = partition
        self.namespace = namespace
        self.name = name
        self.work_mode = work_mode
        self.storage_engine = storage_engine
        self.storage_address = storage_address
        self.destroy = destroy

    def check(self):
        return True

