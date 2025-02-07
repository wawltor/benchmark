#   Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common_import import *


@benchmark_registry.register("compare")
class CompareConfig(APIConfig):
    def __init__(self):
        super(CompareConfig, self).__init__('compare')
        self.api_name = 'less_than'
        self.api_list = {
            'less_than': 'lt',
            'less_equal': 'le',
            'not_equal': 'ne',
            'greater_than': 'gt',
            'greater_equal': 'ge',
            'equal': 'eq'
        }

        # TODO(Xreki): the api of tf and pytorch is different.

    #        self.api_list = {
    #            'less_than': 'less',
    #            'less_equal': 'less_equal',
    #            'not_equal': 'not_equal',
    #            'greater_than': 'greater',
    #            'greater_equal': 'greater_equal',
    #            'equal': 'equal'
    #        }


@benchmark_registry.register("compare")
class PaddleCompare(PaddleOpBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name='x', shape=config.x_shape, dtype=config.x_dtype)
        y = self.variable(name='y', shape=config.y_shape, dtype=config.y_dtype)
        result = self.layers(config.api_name, x=x, y=y)

        self.feed_list = [x, y]
        self.fetch_list = [result]


@benchmark_registry.register("compare")
class TorchCompare(PytorchOpBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name='x', shape=config.x_shape, dtype=config.x_dtype)
        y = self.variable(name='y', shape=config.y_shape, dtype=config.y_dtype)
        result = self.layers(config.api_name, input=x, other=y)

        self.feed_list = [x, y]
        self.fetch_list = [result]


@benchmark_registry.register("compare")
class TFCompare(TensorflowOpBenchmarkBase):
    def build_graph(self, config):
        x = self.variable(name='x', shape=config.x_shape, dtype=config.x_dtype)
        y = self.variable(name='y', shape=config.y_shape, dtype=config.y_dtype)
        result = self.layers(config.api_name, x=x, y=y)

        self.feed_list = [x, y]
        self.fetch_list = [result]
