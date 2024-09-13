import torch
import numpy as np

from config import config
from sparsemask_api.sparse_mask_eval_mode import SparseMask


def sparsemask(mask, weights):
    # load arch
    mask = np.load(mask)
    model = SparseMask(mask,
                       backbone_name="mobilenet_v2",
                       depth=64,
                       in_channels=3,
                       num_classes=config.num_classes)

    # load weight
    weights_dict = torch.load(weights, map_location="cpu")
    weights_dict = {key.replace(
        "module.", ""): value for key, value in weights_dict['state_dict'].items()}
    model.load_state_dict(weights_dict, strict=False)

    return dict(model=model, name="SparseMask")
