import pytest
import graphics.taa_jitter_reject as mod

CASES = [
    ("jitter_by_time", (1,)),
    ("motion_current_matrix", (1,)),
    ("adaptive_blend", (1,)),
    ("depth_weight_clip", (1,)),
    ("clear_on_switch", (1,)),
    ("clamp_output", (1,)),
    ("jitter", (1,)),
    ("reproject", (1,)),
    ("blend", (1,)),
    ("resolve", (1,)),
    ("validate_history", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
