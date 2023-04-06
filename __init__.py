from .QualityOfLifeSuit_Omar92 import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_SUIT
from .QualityOfLife_deprecatedNodes import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_DEPRECATED

try:
    from .QualityOfLife_deprecatedNodes import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_DEPRECATED
except ImportError:
    NODE_CLASS_MAPPINGS_DEPRECATED = {}


__all__ = ['NODE_CLASS_MAPPINGS_SUIT', 'NODE_CLASS_MAPPINGS_DEPRECATED', 'NODE_CLASS_MAPPINGS']
NODE_CLASS_MAPPINGS = {
    **NODE_CLASS_MAPPINGS_SUIT,
    **NODE_CLASS_MAPPINGS_DEPRECATED
}