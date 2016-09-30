from .network import Net
from _caffe import (
    Layer,
    SGDSolver,
    NesterovSolver,
    AdaGradSolver,
    RMSPropSolver,
    AdaDeltaSolver,
    AdamSolver,
    set_mode_cpu,
    set_mode_gpu,
    set_device,
    get_solver,
    layer_type_list,
    set_random_seed,
    __version__
)

from .proto.caffe_pb2 import TRAIN, TEST
