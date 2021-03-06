# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class RenameFaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'RenameFace','cloudphoto')
		self.set_protocol_type('https');

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_FaceId(self):
		return self.get_query_params().get('FaceId')

	def set_FaceId(self,FaceId):
		self.add_query_param('FaceId',FaceId)

	def get_FaceName(self):
		return self.get_query_params().get('FaceName')

	def set_FaceName(self,FaceName):
		self.add_query_param('FaceName',FaceName)