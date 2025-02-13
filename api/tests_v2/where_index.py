#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
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


class PDWhereIndex(PaddleAPIBenchmarkBase):
    def build_program(self, config):
        data = self.variable(
            name='x', shape=config.x_shape, dtype=config.x_dtype)
        # paddle.where invoke paddle.fluid.core.ops.where_index
        value = paddle.fluid.layers.where(data)

        self.feed_vars = [data]
        self.fetch_vars = [value]
        print(self.fetch_vars)


class TFWhereIndex(TensorflowAPIBenchmarkBase):
    def build_graph(self, config):
        data = self.variable(
            name='x', shape=config.x_shape, dtype=config.x_dtype)
        value = tf.where(data)

        self.feed_list = [data]
        self.fetch_list = [value]
        print(self.fetch_list)


if __name__ == '__main__':
    test_main(PDWhereIndex(), TFWhereIndex(), config=APIConfig("where_index"))
